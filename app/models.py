from app.database import get_connection

def criar_tabelas():
    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            sobrenome TEXT NOT NULL,
            idade INTEGER,
            peso REAL,
            altura REAL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exercises (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            nome_exercicio TEXT NOT NULL,
            series INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')
    
    conn.commit()
    conn.close()


def adicionar_usuario(nome, sobrenome, idade, peso, altura):
    conn = get_connection()
    cursor = conn.cursor()
    
    
    cursor.execute('''
        INSERT INTO users (nome, sobrenome, idade, peso, altura) 
        VALUES (?, ?, ?, ?, ?)
    ''', (nome, sobrenome, idade, peso, altura))
    
    conn.commit()
    conn.close()