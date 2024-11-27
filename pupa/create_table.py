import sqlite3
import hashlib

def create_table():
    # Устанавливаем соединение с базой данных SQLite.
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()

    # SQL-запрос для создания таблицы
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    ''')

    conn.commit()
    cur.close()
    conn.close()

def insert_user(email, password):
    # Устанавливаем соединение с базой данных SQLite.
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()

    # Хешируем пароль для безопасного хранения
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

    try:
        # SQL-запрос для вставки нового пользователя
        cur.execute('''
            INSERT INTO users (email, password_hash)
            VALUES (?, ?)
        ''', (email, password_hash))

        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error inserting user: {e}")
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    create_table()

    # Пример добавления пользователя
    email = 'user@example.com'
    password = 'securepassword'
    insert_user(email, password)
    print("User inserted successfully.")