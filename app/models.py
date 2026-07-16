from app.Database import get_connection

def criar_tabelas():
    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS users (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                   idade integer
                   )
                   ''')
    
    Cursor.execute('''
            CREATE TABLE IF NOT EXISTS exercises (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   USER_id INTEGER NOT NULL,
                   series INTEGER,
                   FOREIGN KEY (USER_id) REFERENCES users(id)
                   )
                   ''')
    conn.commit()
    conn.close()
    

