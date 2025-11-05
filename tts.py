from gtts import gTTS
import uuid
import os

def text_to_speech(text, lang_code="hi"):
    # Guarantee static/media/ exists
    audio_dir = os.path.join("static", "media")
    os.makedirs(audio_dir, exist_ok=True)
    filename = f"output_{lang_code}_{uuid.uuid4().hex[:8]}.mp3"
    path = os.path.join(audio_dir, filename)
    tts = gTTS(text=text, lang=lang_code)
    tts.save(path)
    return filename  # just filename, not full path
