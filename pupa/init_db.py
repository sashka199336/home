import sqlite3

def create_table():
    # Устанавливаем соединение с базой данных SQLite.
    # Если файла базы данных не существует, он будет создан.
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

    # Сохраняем изменения
    conn.commit()

    # Закрываем курсор и соединение
    cur.close()
    conn.close()

if __name__ == '__main__':
    create_table()