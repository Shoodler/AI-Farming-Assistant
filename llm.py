import os
import pickle
import faiss
from openai import OpenAI
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

# Load environment variables
load_dotenv()

# Load FAISS Knowledge Base
FAISS_PATH = "rag/vector_index.faiss"
DOCS_PATH = "rag/docs.pkl"

# Load embedding model once
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index + docs at startup
try:
    index = faiss.read_index(FAISS_PATH)
    with open(DOCS_PATH, "rb") as f:
        docs = pickle.load(f)  # now docs is list of dicts: {"text": ..., "doc_name": ...}
    print(f"[RAG] Loaded FAISS index with {index.ntotal} entries.")
except Exception as e:
    print(f"[RAG] Warning: Could not load FAISS knowledge base: {e}")
    index = None
    docs = []

def retrieve_context(query, top_k=3):
    """Retrieve top matching chunks from FAISS based on query."""
    if index is None or not docs:
        return ""

    query_emb = embed_model.encode([query])
    distances, indices = index.search(query_emb, top_k)

    retrieved_chunks = []
    for i in indices[0]:
        if i < len(docs):
            chunk = docs[i]
            # gracefully fallback in case docs were old format
            text = chunk["text"] if isinstance(chunk, dict) and "text" in chunk else str(chunk)
            docname = chunk.get("doc_name", "Unknown Document") if isinstance(chunk, dict) else "Unknown Document"
            retrieved_chunks.append(f"[{docname}] {text}")

    return "\n".join(retrieved_chunks)

# Initialize Groq client
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def query_llm(question, lang_code="hi"):
    """
    Query Groq LLM with friendly farming assistant style + RAG context usage.
    """
    # Retrieve relevant chunks
    context = retrieve_context(question)

    system_prompt = f"""
You are a friendly, expert AI Farming Assistant designed to help with farming, agriculture, and government farming schemes.

Your answers should sound natural, smooth, and conversational — like you are speaking directly to a real person, in simple terms.

Important rules for your answers:
- Always use simple, clear language people can understand.
- Do not use bullet points, lists, numbered points, markdown, or any special formatting.
- Speak in full sentences that flow logically and gently guide the conversation.
- Explain things step-by-step as if explaining to a friend, but keep it brief, calm, and supportive.

If helpful, use the information from the context below when forming your answer. Never mention the context directly — just include the relevant information smoothly in your reply.

You must always:
- If you refer to something from the context, mention the document/source name naturally.
  For example: "According to the document 'Crop Rotation Guide.pdf', crop rotation improves soil health..."
- If multiple relevant pieces are found, include them naturally and name each source.
- If no relevant context matches the question, answer using general farming knowledge.
- Never make up facts.
- If the question is unrelated to farming or agricultural schemes, respond with:
  "Sorry, your question is outside the scope of farming and related schemes, so I cannot answer that."

Context (use only if relevant):
{context}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        temperature=0.3,
        max_tokens=600
    )

    answer = response.choices[0].message.content.strip()
    return answer
