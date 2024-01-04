import sqlite3
con = sqlite3.connect('lms.db')
cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS books (
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            amount INTEGER NOT NULL,
            PRIMARY KEY (title, author)
    )
''')
con.commit()
con.close()