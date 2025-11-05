# rag/query_index.py
import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer

INDEX_PATH = "rag/vector_index.faiss"
DOCS_PATH = "rag/docs.pkl"

embed_model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index(INDEX_PATH)
with open(DOCS_PATH, "rb") as f:
    docs = pickle.load(f)  # list of (chunk_text, doc_name)

def retrieve_context(query, top_k=3):
    query_emb = embed_model.encode([query])
    distances, indices = index.search(query_emb, top_k)

    results = []
    for i in indices[0]:
        if 0 <= i < len(docs):
            chunk_text, doc_name = docs[i]
            results.append((chunk_text, doc_name))

    return results
