import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    # Создаем таблицу users
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            phone TEXT UNIQUE NOT NULL,
            is_authorized INTEGER DEFAULT 0
        )
    ''')
    
    conn.commit()
    conn.close()
    print("База данных успешно инициализирована!")

if __name__ == '__main__':
    init_db() 