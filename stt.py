import whisper
from utils import map_lang_code

model = whisper.load_model("small")  # lightweight for local

def speech_to_text(file_path, lang_choice="Auto-detect"):
    result = model.transcribe(file_path)
    text = result["text"]

    if lang_choice == "Auto-detect":
        detected_lang = map_lang_code(result["language"])
    else:
        detected_lang = lang_choice.lower()[:2]

    return text, detected_lang
