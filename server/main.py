import os
import json
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import traceback
from openai import OpenAI
import uuid

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

import os
import json
import uuid
import traceback
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app = FastAPI()

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/videos", StaticFiles(directory="videos"), name="videos")

session_histories = {}
session_points = {}

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.post("/chat")
async def chat(req: ChatRequest, request: Request):
    try:
        session_id = request.cookies.get('session_id') or str(uuid.uuid4())
        
        if session_id not in session_histories:
            session_histories[session_id] = []
            session_points[session_id] = 0
            
        conversation_history = session_histories[session_id]
        total_points = session_points[session_id]

        conversation_history.append({"role": "user", "content": req.message})
        
        print(req.message)

        response_content = get_response_content(req.message, client, conversation_history)
        
        if response_content is None:
            raise HTTPException(status_code=500, detail="Failed to get response from AI")

        try:
            response_obj = json.loads(response_content)
 
            if "messages" in response_obj:
                messages = response_obj["messages"]
            else:
                # Tenta encontrar qualquer chave que contenha array
                for key, value in response_obj.items():
                    if isinstance(value, list):
                        messages = value
                        break
                else:
                    raise Exception("No 'messages' array found in response")
            
            if not isinstance(messages, list):
                raise Exception("'messages' is not a list")
        except Exception as e:
            raise Exception(f"Error parsing OpenAI response as JSON array: {e}")
        
        conversation_history.append({
            "role": "assistant",
            "content": response_content
        })
        print(response_content)

        # Points
        for message in messages:
            points = message.get("points", 0)

            if points:
                total_points += points

            session_points[session_id] = total_points
            message["total_points"] = total_points

        # Audio
        # for i, message in enumerate(messages):
        #     file_path = f"audios/audio.mp3"
        #     text_input = message.get("text", "")

        #     try:
        #         generate_speech(client, text_input, file_path)

        #         if not os.path.exists(file_path):
        #             raise Exception(f"Arquivo {file_path} não encontrado após geração.")

        #         message["audio"] = await audio_file_to_base64(file_path)
        #         print(message["audio"])

        #     except Exception as e:
        #         message["audio"] = None

        # Vídeos
        for message in messages:
            video = message.get("video_url", "")
            if video:
                message["video_url"] = f"videos/{video}.mp4"

        session_histories[session_id] = conversation_history

        response = JSONResponse({
            "session_id": session_id,
            "messages": messages
        })
        response.set_cookie(key="session_id", value=session_id)

        print(response)
        return response

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
