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
    
def create_post(content: str, user_id: int):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO publicacao_gs (id, conteudo, data_publicacao, id_usuario)
        VALUES (id_publicacao.nextval, :content, null, :user_id )
    """, [content, user_id])
    conn.commit()
    cursor.close()
    
    return True

def get_posts():
    cursor = conn.cursor()
    cursor.execute("""
        SELECT publicacao_gs.id, usuario_gs.nome, publicacao_gs.conteudo, publicacao_gs.data_publicacao FROM usuario_gs
        LEFT JOIN publicacao_gs ON usuario_gs.id = publicacao_gs.id_usuario
    """)
    result = cursor.fetchall()
    conn.commit()
    cursor.close()
    
    return result

def delete_post(post_id: int):
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM publicacao_gs
        WHERE publicacao_gs.id = :post_id
    """, [post_id])
    conn.commit()
    cursor.close()
    
    return True