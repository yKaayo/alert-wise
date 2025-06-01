import os
import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import traceback
import asyncio

# Files
from services.audio import elevenlabs_text_to_speech, audio_file_to_base64
from services.ai import get_response_content
from schemas import ChatRequest

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/videos", StaticFiles(directory="videos"), name="videos")

# Keys
# eleven_labs_api_key = os.getenv("ELEVEN_LABS_API_KEY")
eleven_labs_api_key = os.getenv("ELEVEN_LABS_API_KE")
voice_id = "uhYnkYTBc711oAY590Ea"

@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        user_message = req.message

        response_content = get_response_content(user_message)
        if response_content is None:
            raise HTTPException(status_code=500, detail="Failed to get response from AI")

        try:
            messages = json.loads(response_content)
            print(messages)

            if not isinstance(messages, list):
                raise Exception("Response JSON is not a list")
        except Exception as e:
            raise Exception(f"Error parsing OpenAI response as JSON array: {e}")

        for i, message in enumerate(messages):
            file_name = f"audios/message_{i}.mp3"
            text_input = message.get("text", "")

            video = message.get("video_url", "")
            video_file_name = f"videos/{video}.mp4"

            try:
                # Audio
                # elevenlabs_text_to_speech(eleven_labs_api_key, voice_id, file_name, text_input)

                # await asyncio.sleep(0.1)

                # if not os.path.exists(file_name):
                #     raise Exception(f"Arquivo {file_name} não encontrado após geração.")

                # message["audio"] = await audio_file_to_base64(file_name)
                # print(message["audio"])

                # Video
                os.makedirs("videos", exist_ok=True)
                
                if not os.path.exists(video_file_name):
                    raise Exception(f"Arquivo de vídeo {video_file_name} não encontrado.")
        
                message["video_url"] = video_file_name

            except Exception as e:
                message["audio"] = None
                message["video_url"] = None

        print(messages)

        return {"messages": messages}

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
