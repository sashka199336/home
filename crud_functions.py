import sqlite3

from module_14.db import cursor, connection


def initiate_db():
    connection = sqlite3.connect('new_db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price TEXT NOT NULL
    )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        );
        ''')

    connection.commit()
    # connection.close()


def add_user(username, email, age):
    cursor.execute(f"INSERT INTO Users (username, email, age, balance) VALUES ('{username}', '{email}', '{age}', 1000)")
    connection.commit()


def is_included(username):
    user = cursor.execute(f"SELECT * FROM Users WHERE username = ?", (username,))
    if user.fetchone() is None:
        return True
    else:
        return False
    connection.commit()

def check_and_populate_products():
    connection = sqlite3.connect('new_db')
    cursor = connection.cursor()

    cursor.execute('SELECT COUNT(*) FROM Products')
    count = cursor.fetchone()[0]

    if count == 0:
        for i in range(1, 5):
            cursor.execute(
                'INSERT INTO Products(title, description, price) VALUES (?, ?, ?)',
                (f'Продукт {i}', f'Описание {i}', f'{i * 100}')
            )
    else:
        pass

    connection.commit()
    # connection.close()


def get_all_products():
    connection = sqlite3.connect('new_db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.commit()
    # connection.close()
    return products
