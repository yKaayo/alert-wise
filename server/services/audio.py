import requests
import base64
import os

os.makedirs("audios", exist_ok=True)

def elevenlabs_text_to_speech(api_key, voice_id, file_name, text_input):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text_input,
        "voice_settings": {
            "stability": 0.75,
            "similarity_boost": 0.75
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    print(response)
    
    if response.status_code != 200 or response.headers.get("Content-Type") != "audio/mpeg":
        raise Exception(f"ElevenLabs API error: {response.text}")
    with open(file_name, "wb") as f:
        f.write(response.content)

async def audio_file_to_base64(file):
    try:
        with open(file, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
            return b64
    except FileNotFoundError:
        return None
    except Exception as e:
        return None
