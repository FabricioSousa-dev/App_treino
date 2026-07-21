import sqlite3

def get_connection():
    '''
    Função para criar uma conexão com o banco de dados SQLite.
    Retorna um objeto de conexão.
    
    '''

    conn = sqlite3.connect('treino.db')

    conn.row_factory = sqlite3.Row
    return conn
