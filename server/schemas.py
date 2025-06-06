from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
    message: str
    user_id: Optional[int] = None
    user_email: Optional[str] = None 

class GetUser(BaseModel):
    email: str
    password: str

class UserCreateUser(BaseModel):
    name: str
    email: str
    password: str
    
class CreatePost(BaseModel):
    name: str
    email: str
    password: str
    content: str
    
class UpdatePost(BaseModel):
    id: int
    content: str