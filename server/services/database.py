import oracledb
from dotenv import load_dotenv
import os

# Utils
from utils.crypt import crypt_password

load_dotenv()

dsn = oracledb.makedsn("oracle.fiap.com.br", 1521, service_name="ORCL")
conn = oracledb.connect(user=os.getenv("DB_EMAIL"), password=os.getenv("DB_PASSWORD"), dsn=dsn)

def verify_user(email: str):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuario_gs WHERE email = :email", [email])
    result = cursor.fetchone()
    cursor.close()

    return result

def get_user(email: str, password: str):
    hashed_password = crypt_password(password)

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuario_gs WHERE email = :email AND senha = :hashed_password", [email, hashed_password])
    result = cursor.fetchone()
    cursor.close()
    
    return result

def create_user(name: str, email: str, password: str):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO usuario_gs (id, nome, email, senha)
        VALUES (id_usuario.NEXTVAL, :name, :email, :senha)
    """, [name, email, password])
    conn.commit()
    cursor.close()
