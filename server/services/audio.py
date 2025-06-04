import base64
import os

os.makedirs("audios", exist_ok=True)

def generate_speech(client, text, file_path):
    with client.audio.speech.with_streaming_response.create(
      model="gpt-4o-mini-tts",
      voice="nova",
      input=text,
      instructions="Speak in a calm and positive tone using portuguese of Brazil.",
  ) as response:
      response.stream_to_file(file_path)

async def audio_file_to_base64(file):
    try:
        with open(file, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
            return b64
    except FileNotFoundError:
        return None
    except Exception as e:
        return None
