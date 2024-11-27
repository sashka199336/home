from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import hashlib

app = Flask(__name__)

def create_table():
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()
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
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    try:
        cur.execute('''
            INSERT INTO users (email, password_hash)
            VALUES (?, ?)
        ''', (email, password_hash))
        conn.commit()
    except sqlite3.IntegrityError as e:
        return False, str(e)
    finally:
        cur.close()
        conn.close()
    return True, "User inserted successfully."

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        success, message = insert_user(email, password)
        if success:
            return redirect(url_for('success'))
        else:
            return f"Error: {message}"
    return render_template('register.html')

@app.route('/success')
def success():
    return "Registration successful!"

if __name__ == '__main__':
    create_table()
    app.run(debug=True)