import os
import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import traceback
from openai import OpenAI

# Files
from services.audio import audio_file_to_base64, generate_speech
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

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        user_message = req.message

        response_content = get_response_content(user_message, client)
        if response_content is None:
            raise HTTPException(status_code=500, detail="Failed to get response from AI")

        try:
            messages = json.loads(response_content)
            print(messages)

            if not isinstance(messages, list):
                raise Exception("Response JSON is not a list")
        except Exception as e:
            raise Exception(f"Error parsing OpenAI response as JSON array: {e}")

        # Audio
        for i, message in enumerate(messages):
            file_path = f"audios/message_{i}.mp3"
            text_input = message.get("text", "")

            try:
                generate_speech(client, text_input, file_path)

                if not os.path.exists(file_path):
                    raise Exception(f"Arquivo {file_path} não encontrado após geração.")

                message["audio"] = await audio_file_to_base64(file_path)
                print(message["audio"])

            except Exception as e:
                message["audio"] = None

        # Video
        for message in messages:
            video = message.get("video_url", "")
            video_file_name = f"videos/{video}.mp4"

            try:
                os.makedirs("videos", exist_ok=True)
                
                if not os.path.exists(video_file_name):
                    raise Exception(f"Arquivo de vídeo {video_file_name} não encontrado.")
        
                message["video_url"] = video_file_name

            except Exception as e:
                message["video_url"] = None


        print(messages)

        return {"messages": messages}

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
