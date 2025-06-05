from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str

class GetUser(BaseModel):
    email: str
    password: str

class UserCreateUser(BaseModel):
    name: str
    email: str
    password: str