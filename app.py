from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import uuid
from stt import speech_to_text
from llm import query_llm
from tts import text_to_speech

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

# Media files under static/media/
MEDIA_DIR = os.path.join(app.static_folder, "media")
os.makedirs(MEDIA_DIR, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")
    lang = request.form.get("lang", "Auto-detect")
    
    if not file:
        return jsonify({"error": "No file uploaded."}), 400
    
    # Save uploaded audio to static/media/
    temp_filename = f"input_{uuid.uuid4().hex}_{file.filename}"
    temp_path = os.path.join(MEDIA_DIR, temp_filename)
    file.save(temp_path)
    
    try:
        user_text, detected_lang = speech_to_text(temp_path, lang)
        ai_resp = query_llm(user_text, detected_lang)
        
        # This now returns the saved filename (not path!)
        tts_filename = text_to_speech(ai_resp, detected_lang)
        audio_url = f"/static/media/{tts_filename}"
        
        result = {
            "query_text": user_text,
            "response_text": ai_resp,
            "audio_url": audio_url
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
