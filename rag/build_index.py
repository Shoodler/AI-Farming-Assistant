# rag/build_index.py
import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
from PyPDF2 import PdfReader

# Folder containing PDFs
DOCS_DIR = "rag/data"
OUTPUT_INDEX = "rag/vector_index.faiss"
OUTPUT_DOCS = "rag/docs.pkl"

embed_model = SentenceTransformer("all-MiniLM-L6-v2")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

all_chunks = []
indexed_meta = []  # (chunk_text, doc_name)

for filename in os.listdir(DOCS_DIR):
    if filename.endswith(".pdf"):
        path = os.path.join(DOCS_DIR, filename)
        print(f"[INFO] Processing: {filename}")

        reader = PdfReader(path)
        raw_text = ""
        for page in reader.pages:
            raw_text += page.extract_text() + "\n"

        chunks = text_splitter.split_text(raw_text)

        for chunk in chunks:
            indexed_meta.append((chunk, filename))
            all_chunks.append(chunk)

print(f"[INFO] Total chunks: {len(all_chunks)}")

embeddings = embed_model.encode(all_chunks, convert_to_numpy=True)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

faiss.write_index(index, OUTPUT_INDEX)
with open(OUTPUT_DOCS, "wb") as f:
    pickle.dump(indexed_meta, f)

print("[SUCCESS] FAISS index + document metadata saved.")
