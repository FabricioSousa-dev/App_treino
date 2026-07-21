from app.database import get_connection

def criar_tabelas():
    '''
    Função para criar as tabelas no banco de dados.
    Não recebe parâmetros e não retorna nada.

    '''
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
    '''
    Função para adicionar um novo usuário ao banco de dados.
    Retorna o ID do usuário adicionado.
    '''
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO users (nome, sobrenome, idade, peso, altura) 
        VALUES (?, ?, ?, ?, ?)
    ''', (nome, sobrenome, idade, peso, altura))

    conn.commit()
    user_id = cursor.lastrowid   # <- pega o id gerado automaticamente
    conn.close()
    return user_id

def adicionar_exercicio(user_id, nome_exercicio, series):
    '''
    Função para adicionar um novo exercício ao banco de dados.
    Não retorna nada.
    '''
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO exercises (user_id, nome_exercicio, series)
        VALUES (?, ?, ?)
    ''', (user_id, nome_exercicio, series))

    conn.commit()
    conn.close()

def listar_usuarios():
    '''
    Função para listar todos os usuários cadastrados no banco de dados.
    Retorna uma lista de usuários.
    '''
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users')
    usuarios = cursor.fetchall()

    conn.close()
    return usuarios



    