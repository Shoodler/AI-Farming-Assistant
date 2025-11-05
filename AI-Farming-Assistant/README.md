# 🌾 AI Farming Helper

<p align="center">
  <img src="https://img.shields.io/badge/Flask-2.0+-blue.svg" alt="Flask">
  <img src="https://img.shields.io/badge/Python-3.8+-green.svg" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
</p>

<p align="center">
  A voice-based multilingual agriculture assistant web application designed to help farmers get instant answers to their farming questions in their native language.
</p>

---

## 📖 Table of Contents

- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Supported Languages](#supported-languages)
- [Agricultural Topics](#agricultural-topics)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## 🌟 About

AI Farming Helper is a web-based voice assistant that empowers farmers to ask agricultural questions in their native language and receive AI-powered responses with audio playback. The application uses state-of-the-art speech recognition, natural language processing, and text-to-speech technologies to bridge the digital divide in agriculture.

Whether you need advice on crop management, pest control, fertilizers, weather conditions, or soil health, AI Farming Helper provides accessible, voice-first interaction designed for users of all literacy levels.

---

## ✨ Features

- 🎤 **Voice Recording**: Record questions directly through your browser's microphone
- 📁 **Audio Upload**: Upload pre-recorded audio files in various formats
- 🌍 **Multi-language Support**: Automatic language detection and support for:
  - Hindi (हिंदी)
  - Marathi (मराठी)
  - Malayalam (മലയാളം)
  - Bengali (বাংলা)
  - Tamil (தமிழ்)
  - Telugu (తెలుగు)
  - Kannada (ಕನ್ನಡ)
  - Gujarati (ગુજરાતી)
  - English
- 🤖 **AI-Powered Responses**: Context-aware answers using Groq's Llama 3.1 model
- 🔊 **Audio Playback**: Natural-sounding voice responses via Google Text-to-Speech
- 📝 **Text Display**: View both your question and the AI's response in text format
- 📱 **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- 🚫 **No Special Hardware**: Runs entirely in the browser with a simple backend

---

## 🛠️ Tech Stack

**Frontend:**
- HTML5
- CSS3 (Modern gradient design)
- Vanilla JavaScript (ES6+)

**Backend:**
- Flask 2.0+ (Python web framework)
- Flask-CORS (Cross-Origin Resource Sharing)

**AI & ML Services:**
- **Speech-to-Text**: OpenAI Whisper (automatic language detection)
- **LLM**: Groq API with Llama 3.1 70B (optimized for conversational responses)
- **Text-to-Speech**: Google Text-to-Speech (gTTS)

**Additional Libraries:**
- python-dotenv (Environment variable management)
- UUID (Unique file naming)

---

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- A modern web browser (Chrome, Firefox, Safari, Edge)
- Microphone access (for voice recording)

### Installation

1. **Clone the repository:**

git clone [https://github.com/yourusername/ai-farming-helper.git](https://github.com/yourusername/ai-farming-helper.git)  
cd ai-farming-helper

2. **Create a virtual environment (recommended):**

```
python -m venv venv

# On Windows

venv\Scripts\activate

# On macOS/Linux

source venv/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

### Configuration

1. **Create a `.env` file in the project root:**
```
touch .env
```

2. **Add your Groq API key to the `.env` file:**

```
GROQ_API_KEY=your_groq_api_key_here
```

**How to get a Groq API key:**
- Visit [Groq Console](https://console.groq.com)
- Sign up for a free account
- Navigate to API Keys section
- Generate a new API key

---

## 💡 Usage

1. **Start the Flask server:**

```bash
python app.py
```

You should see output similar to:

- Running on [http://127.0.0.1:5000](http://127.0.0.1:5000/)
- Debug mode: on

2. **Open your browser and navigate to:**
[http://127.0.0.1:5000](http://127.0.0.1:5000/)


3. **Ask a question:**

   **Method 1: Voice Recording**
   - Click the "Press to Speak" button
   - Allow microphone access when prompted
   - Speak your farming question clearly
   - Click the button again to stop recording
   - Wait for the AI response

   **Method 2: Audio Upload**
   - Click "Upload Audio File"
   - Select an audio file from your device
   - Wait for the AI response

4. **View the results:**
   - Your question (transcribed text)
   - AI's response (text)
   - Audio playback of the response

---

## 📁 File Structure

```
ai-farming-helper/  
│  
├── app.py # Flask application & routing  
├── stt.py # Speech-to-text module (Whisper)  
├── llm.py # Language model interaction (Groq)  
├── tts.py # Text-to-speech module (Google TTS)  
├── utils.py # Utility functions (language mapping)  
├── requirements.txt # Python dependencies  
├── .env # Environment variables (not in repo)  
├── .gitignore # Git ignore file  
├── README.md # Project documentation  
│  
├── templates/  
│ └── index.html # Main web interface  
│  
└── static/  
├── css/  
│ └── styles.css # Stylesheet  
├── js/  
│ └── script.js # Frontend JavaScript  
└── media/ # Generated audio files (auto-created)  
└── output_*.mp3 # AI response audio files
```


---

## 🌍 Supported Languages

| Language | Code | Native Name |
|----------|------|-------------|
| Auto-detect | `Auto-detect` | Automatic |
| English | `en` | English |
| Hindi | `hi` | हिन्दी |
| Marathi | `mr` | मराठी |
| Malayalam | `ml` | മലയാളം |
| Bengali | `bn` | বাংলা |
| Tamil | `ta` | தமிழ் |
| Telugu | `te` | తెలుగు |
| Kannada | `kn` | ಕನ್ನಡ |
| Gujarati | `gu` | ગુજરાતી |

---

## 🌱 Agricultural Topics

The AI assistant is knowledgeable in the following areas:

### 🌾 Crop Management
- Planting schedules and techniques
- Irrigation best practices
- Harvesting guidance
- Crop rotation strategies

### 🐛 Pest & Disease Control
- Pest identification
- Disease symptoms and diagnosis
- Organic and chemical treatment options
- Prevention strategies

### 💧 Fertilizers & Soil Health
- Nutrient management
- Soil testing and analysis
- Fertilizer recommendations
- Composting and organic amendments

### ☀️ Weather & Climate
- Seasonal planning
- Weather-based decision making
- Climate adaptation strategies
- Drought and flood management

---

## 🔧 Troubleshooting

### Audio doesn't play
- Check if MP3 files are being generated in `static/media/`
- Verify browser supports HTML5 audio
- Check browser console for errors

### Microphone not working
- Ensure you've granted microphone permissions in your browser
- Try using HTTPS (microphone API requires secure context)
- Check if another application is using the microphone

### API errors
- Verify your Groq API key is correct in `.env`
- Check your API quota/limits
- Ensure you have internet connectivity

### Language detection issues
- Speak clearly and at a moderate pace
- Reduce background noise
- Manually select language if auto-detect fails

### Flask server won't start
- Check if port 5000 is already in use
- Verify all dependencies are installed
- Check Python version (3.8+ required)

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Contribution
- Add support for more Indian languages
- Implement offline mode with cached responses
- Add visual disease identification using image upload
- Create mobile app versions (iOS/Android)
- Improve UI/UX design
- Add unit tests and integration tests

---

## 📄 License

Distributed under the MIT License. See `LICENSE` file for more information.

---

<p align="center">
  Made with ❤️ for farmers
</p>

<p align="center">
  ⭐ Star this repository if you find it helpful!
</p>



