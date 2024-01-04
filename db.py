import sqlite3

def connect_to_db():
    con = sqlite3.connect('lms.db')
    return con


def insert_book(title, author, amount):
    con = connect_to_db()
    cur = con.cursor()
    cur.execute('INSERT INTO books (title, author, amount) VALUES (?,?,?)',(title, author, amount))
    close_connection(con)

def fetch_book():
    con = connect_to_db()
    cur = con.cursor()
    cur.execute('SELECT * FROM books')
    rows = cur.fetchall()
    close_connection(con)
    return rows


def close_connection(con):
    con.commit()
    con.close()