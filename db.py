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

def find_book(title, author):
    con = connect_to_db()
    cur = con.cursor()
    if title!=None and author!=None:
        cur.execute('SELECT * FROM books WHERE title = ? and author = ?', (title, author))
    elif title!=None:
        cur.execute('SELECT * FROM books WHERE title = ? ', (title,))
    elif author!=None:
        cur.execute('SELECT * FROM books WHERE author = ?', (author))
    else:
        cur.execute('SELECT * FROM books')

    rows = cur.fetchall()
    close_connection(con)
    return rows

def delete_book(title, author):
    con = connect_to_db()
    cur = con.cursor()
    cur.execute('DELETE FROM books WHERE title = ? and author = ?', (title, author))
    close_connection(con)

def update_book():
    pass


def close_connection(con):
    con.commit()
    con.close()