import os
import json
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import traceback
from openai import OpenAI
from fastapi.responses import JSONResponse

# Database
from services.database import create_user, get_user, add_user_points, get_posts, delete_post, update_post, create_post

# Schemas
from schemas import UserCreateUser, GetUser, CreatePost, UpdatePost

# Files
from services.audio import audio_file_to_base64, generate_speech
from services.ai import get_response_content
from schemas import ChatRequest

# Utils
from utils.crypt import crypt_password, verify_password
from utils.session import get_current_user

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app.mount("/videos", StaticFiles(directory="videos"), name="videos")

@app.post("/cadastrar")
def signup(user: UserCreateUser):
    hashed_password = crypt_password(user.password)

    if get_user(user.email):
        raise HTTPException(status_code=409, detail="Usuário já existe")
    
    create_user(name=user.name, email=user.email, password=hashed_password)
    return {"messages": "Usuário registrado com sucesso"}

@app.post("/entrar")
def login(user: GetUser):
    user_record = get_user(user.email)

    if not user_record:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    stored_hash = user_record[3]

    if not verify_password(user.password, stored_hash):
        raise HTTPException(status_code=401, detail="Senha incorreta")
    
    return {"message": "Login bem-sucedido!", "login": True, "user_id": user_record[0], "user_email": user_record[2]}

@app.get("/relatos")
def get_reports():
    reports = get_posts()
    
    if not reports:
        raise HTTPException(status_code=500, detail="Erro ao buscar os relatos!")
    
    return reports

@app.post("/relato")
def create_report(post: CreatePost):
    user_record = login(user=GetUser(email=post.email, password=post.password))
    if user_record["login"] is False:
        raise HTTPException(status_code=401, detail="Usuário não autenticado")
    
    user_id = user_record["user_id"]
    create_post(content=post.content, user_id=user_id)
    
    return {"message": "Relato criado com sucesso!"}

@app.delete("/relato")
def delete_report(post_id: int):
    report = delete_post(post_id)
    
    if not report:
        raise HTTPException(status_code=500, detail="Erro ao deletar o relato")
    
    return {"message": "Relato deletado com sucesso!"}

@app.put("/relato")
def update_report(post: UpdatePost):
    post_updated = update_post(post_id=post.id, content=post.content)
    
    if not post_updated:
        raise HTTPException(status_code=500, detail="Erro ao atualizar o relato")
    
    return {"message": "Rota de atualização de relatos ainda não implementada"}

session_histories = {}
session_points = {}
@app.post("/chat")
async def chat(req: ChatRequest, current_user: dict = Depends(get_current_user)):
    try:
        user_id = current_user[0]
        user_identifier = f"user_{user_id}"
        
        if user_identifier not in session_histories:
            session_histories[user_identifier] = []
            session_points[user_identifier] = 0
            
        conversation_history = session_histories[user_identifier]
        total_points = session_points[user_identifier]

        conversation_history.append({"role": "user", "content": req.message})

        response_content = get_response_content(req.message, client, conversation_history)
        
        if response_content is None:
            raise HTTPException(status_code=500, detail="Failed to get response from AI")

        try:
            response_obj = json.loads(response_content)
 
            if "messages" in response_obj:
                messages = response_obj["messages"]
            else:
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

        # Points
        for message in messages:
            points = message.get("points", 0)
            print(points)
            
            if isinstance(points, (int)) and points > 0:
                total_points += points
                add_user_points(points, user_id)
            
            session_points[user_identifier] = total_points
            message["total_points"] = total_points

        # Audio
        for i, message in enumerate(messages):
            file_path = f"audios/audio.mp3"
            text_input = message.get("text", "")

            try:
                generate_speech(client, text_input, file_path)

                if not os.path.exists(file_path):
                    raise Exception(f"Arquivo {file_path} não encontrado após geração.")

                message["audio"] = await audio_file_to_base64(file_path)

            except Exception as e:
                message["audio"] = None

        # Vídeos
        for message in messages:
            video = message.get("video_url", "")
            if video:
                message["video_url"] = f"videos/{video}.mp4"

        print(conversation_history)
        session_histories[user_identifier] = conversation_history

        response = JSONResponse({
            "user_id": user_id,
            "user_email": req.user_email,
            "messages": messages
        })

        return response

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
    