import sqlite3
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
            issued_book TEXT,
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            UNIQUE(name, issued_book)
    )
''')

con.commit()
con.close()

