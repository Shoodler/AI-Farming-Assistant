# README.md


# AI Farming Helper (Flask Version)

A voice-based agriculture assistant web app. Record or upload audio, get instant spoken-friendly answers and MP3 playback.

## Features

- Upload or record audio questions
- Automatic speech-to-text conversion (Whisper/STT)
- AI response via LLM model (Groq/OpenAI/Llama, etc.)
- Text-to-speech MP3 output (Google TTS)
- Audio and text displayed in the browser

## How to Run

1. **Install dependencies:**

    ```
    pip install -r requirements.txt
    ```

2. **Start the Flask server:**

    ```
    python app.py
    ```

3. **Open your browser at:**

    [http://127.0.0.1:5000](http://127.0.0.1:5000)

4. **Usage:**
   - Click "Press to Speak" or upload an audio file.
   - Wait for the assistant’s response and listen in the browser!

## File Structure

```
yourapp/
├── app.py
├── stt.py
├── llm.py
├── tts.py
├── utils.py
├── requirements.txt
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── script.js
│   └── media/
│       └── (output MP3 files)
├── templates/
│   └── index.html
```

## Troubleshooting

- If audio does not play, check `static/media/` for MP3 files.
- Make sure your browser sources CSS/JS using Flask’s `url_for`.
- All audio URLs start with `/static/media/`.

---

# requirements.txt

```
flask
flask-cors
gtts
whisper
openai
python-dotenv
```
*Add/remove dependencies based on your actual model (Groq, Llama, etc.).*
