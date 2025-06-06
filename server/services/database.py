import oracledb
from dotenv import load_dotenv
import os

# Utils
from utils.crypt import crypt_password

load_dotenv()

dsn = oracledb.makedsn("oracle.fiap.com.br", 1521, service_name="ORCL")
conn = oracledb.connect(user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"), dsn=dsn)

def get_user(email: str):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuario_gs WHERE email = :email", [email])
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

def add_user_points(points: int, user_id: int):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO jogo_gs (id, pontos, id_usuario) 
        VALUES ( id_jogo.nextval, :points, :user_id )
        """, [points, user_id])
    conn.commit()
    cursor.close()
    
def create_post(name: str, email: str, password: str, title: str, content: str, date_published: str):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO publicacao_gs (id, titulo, conteudo, data_publicacao, id_usuario)
        VALUES (id_publicacao.nextval, :title, :content, TO_DATE(:date_published, 'DD/MM/YYYY'), :title, :content, )
    """, [name, email, password, title, content, date_published])
    conn.commit()
    cursor.close()
    
    return True
    