import sqlite3
from datetime import datetime
con = sqlite3.connect('lms.db')
cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS books (
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            amount INTEGER NOT NULL,
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            UNIQUE(title, author)
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS students (
            name TEXT NOT NULL,
            id INTEGER PRIMARY KEY
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS lending_record (
            student_id INTEGER NOT NULL UNIQUE,
            issued_book_id INTEGER NOT NULL,
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            FOREIGN KEY (student_id) REFERENCES students(id),
            FOREIGN KEY (issued_book_id) REFERENCES books(id),
            UNIQUE(student_id, issued_book_id)
    )
''')

con.commit()
con.close()

