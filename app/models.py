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
            user_id INTEGER NOT NULL,
            nome_exercicio TEXT NOT NULL,
            series INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
        )
    ''')

    conn.commit()
    conn.close()


# ---------- USUÁRIOS ----------

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
    user_id = cursor.lastrowid
    conn.close()
    return user_id


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


def buscar_usuario_por_id(user_id):
    '''
    Função para buscar um único usuário pelo ID.
    Retorna a linha do usuário ou None se não existir.
    '''
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    usuario = cursor.fetchone()

    conn.close()
    return usuario


def deletar_usuario(user_id):
    '''
    Função para deletar um usuário e, em cascata, seus exercícios.
    Retorna True se algum usuário foi deletado, False caso contrário.
    '''
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    deletado = cursor.rowcount > 0
    conn.close()
    return deletado


# ---------- EXERCÍCIOS ----------

def adicionar_exercicio(user_id, nome_exercicio, series):
    '''
    Função para adicionar um novo exercício vinculado a um usuário.
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


def listar_exercicios():
    '''
    Função para listar todos os exercícios cadastrados no banco de dados,
    de todos os usuários.
    Retorna uma lista de exercícios.
    '''
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM exercises')
    exercicios = cursor.fetchall()

    conn.close()
    return exercicios


def listar_exercicios_por_usuario(user_id):
    '''
    Função para listar os exercícios de um usuário específico.
    Retorna uma lista de exercícios daquele usuário.
    '''
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM exercises WHERE user_id = ?', (user_id,))
    exercicios = cursor.fetchall()

    conn.close()
    return exercicios


def atualizar_exercicio(exercicio_id, nome_exercicio=None, series=None):
    '''
    Função para atualizar o nome e/ou as séries de um exercício existente.
    Só atualiza os campos informados. Não retorna nada.
    '''
    conn = get_connection()
    cursor = conn.cursor()

    if nome_exercicio is not None:
        cursor.execute(
            'UPDATE exercises SET nome_exercicio = ? WHERE id = ?',
            (nome_exercicio, exercicio_id)
        )
    if series is not None:
        cursor.execute(
            'UPDATE exercises SET series = ? WHERE id = ?',
            (series, exercicio_id)
        )

    conn.commit()
    conn.close()


def deletar_exercicio(exercicio_id):
    '''
    Função para deletar um exercício pelo ID.
    Retorna True se algum exercício foi deletado, False caso contrário.
    '''
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM exercises WHERE id = ?', (exercicio_id,))
    conn.commit()
    deletado = cursor.rowcount > 0
    conn.close()
    return deletado