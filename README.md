# 🧑‍🌾 Voice-Based Farming Assistant (RAG + Groq + FAISS)

This project is an AI-powered **voice-interactive farming assistant** designed to help farmers ask questions using speech and receive clear, natural spoken guidance related to **agriculture, crops, soil, irrigation, pests, weather, livestock, and government farming schemes**.

The system uses:
- **Speech-to-Text (STT)** to convert user audio into text
- **RAG (Retrieval-Augmented Generation)** using **FAISS** to search relevant information from stored documents
- **Groq LLaMA-3.1** for fast, low-latency LLM reasoning
- **Text-to-Speech (TTS)** using gTTS to generate a spoken reply
- A simple browser UI for seamless interaction

## 📂 Project Structure

```
project/
│   app.py
│   llm.py
│   stt.py
│   tts.py
│   utils.py
│   requirements.txt
│   .env
│
├───rag
│   ├── build_index.py
│   ├── query_index.py
│   ├── vector_index.faiss
│   ├── docs.pkl
│   └── data/
│
├───static
│   ├── css/
│   ├── js/
│   └── media/
│
└───templates
    └── index.html
```

## 🚀 Running Locally

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Add your API key in `.env`
```
GROQ_API_KEY=your_api_key_here
```

### 3. Build FAISS Index
```bash
python rag/build_index.py
```

### 4. Start Server
```bash
python app.py
```

Visit http://127.0.0.1:5000/

## 🎙 Voice Flow

User speaks → STT → Retrieve context via FAISS → LLM answer → gTTS → Audio playback

## 🌍 Deployment (Hugging Face Spaces)

Prepare Dockerfile, push project, and set `GROQ_API_KEY` as HF secret.
