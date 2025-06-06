from fastapi import FastAPI, HTTPException, Depends, Request

# Database
from services.database import get_user

def get_current_user(request: Request):
    user_id = request.headers.get("user-id")
    user_email = request.headers.get("user-email")
    
    if not user_id or not user_email:
        raise HTTPException(status_code=401, detail="Não autorizado - cabeçalhos faltando")

    user = get_user(user_email)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    if str(user[0]) != user_id:
        raise HTTPException(status_code=403, detail="Acesso não autorizado")
    
    return user