import sqlite3
# Create database
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fname TEXT, lname TEXT, phone TEXT, age INTEGER, gender TEXT,
            address TEXT, education TEXT, employment TEXT, lang_known TEXT,
            skills TEXT, learn_skills TEXT, mode TEXT, time TEXT,
            job TEXT, shift TEXT, experience TEXT, salary INTEGER
        )
    ''')
    conn.commit()
    conn.close()