import os

def save_audio_file(uploaded_file):
    save_path = f"temp_{uploaded_file.name}"
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return save_path

def map_lang_code(code):
    lang_map = {
        "hi": "hi", "mr": "mr", "ml": "ml", "bn": "bn"
    }
    return lang_map.get(code, "hi")

def detect_language(code):
    """
    Wrapper around map_lang_code for consistency
    """
    return map_lang_code(code)
