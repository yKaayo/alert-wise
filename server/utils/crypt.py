from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def crypt_password(password: str):
    hashed_password = pwd_context.hash(password)
    return hashed_password

def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)