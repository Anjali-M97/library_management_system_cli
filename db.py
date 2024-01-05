import sqlite3
import tables

def connect_to_db():
    con = sqlite3.connect('lms.db')
    return con


def insert_book(title, author, amount):
    con = connect_to_db()
    cur = con.cursor()
    try:
        cur.execute('INSERT INTO books (title, author, amount) VALUES (?,?,?)',(title, author, amount))
    except:
        print('The book already exists.')
    close_connection(con)

def fetch_book():
    con = connect_to_db()
    cur = con.cursor()
    cur.execute('SELECT * FROM books')
    rows = cur.fetchall()
    close_connection(con)
    return rows

def view_record(name, title):
    con = connect_to_db()
    cur = con.cursor()

    if title!=None and name!=None:
        cur.execute('SELECT * FROM students WHERE issued_book = ? and name = ?', (title, name))
    elif title!=None and name==None:
        cur.execute('SELECT * FROM students WHERE issued_book = ?', (title,))
    elif title==None and name!=None:
        cur.execute('SELECT * FROM students WHERE name = ?', (name,))
    else:
        cur.execute('SELECT * FROM students')
    rows = cur.fetchall()
    close_connection(con)
    return rows

def return_book(sname, id):
    con = connect_to_db()
    cur = con.cursor()
    cur.execute('SELECT title FROM books WHERE id = ?', (id,))
    book = cur.fetchall()
    try:
        book = book[0]
        book = book[0]
        cur.execute('SELECT id FROM students WHERE name = ? AND issued_book= ?', (sname, book))
        sid = cur.fetchall()
        sid = sid[0]
        sid = sid[0]
        cur.execute('DELETE FROM students WHERE id = ?', (sid,))
        cur.execute('UPDATE books SET amount = amount + 1 WHERE id = ?', (id,))
    except:
        print ('No such book or book is not issued to the student...')
    close_connection(con)



def find_book(title, author, id):
    con = connect_to_db()
    cur = con.cursor()
    if id!=None:
        cur.execute('SELECT * FROM books WHERE id = ?', (id,))
    elif title!=None and author!=None:
        cur.execute('SELECT * FROM books WHERE title = ? and author = ?', (title, author))
    elif title!=None:
        cur.execute('SELECT * FROM books WHERE title = ? ', (title,))
    elif author!=None:
        cur.execute('SELECT * FROM books WHERE author = ?', (author,))
    else:
        cur.execute('SELECT * FROM books')

    rows = cur.fetchall()
    close_connection(con)
    return rows

def delete_book(id):
    con = connect_to_db()
    cur = con.cursor()
    cur.execute('DELETE FROM books WHERE id = ?', (id,))
    close_connection(con)

def update_book(title, author, amount, id):
    con = connect_to_db()
    cur = con.cursor()
    if title!=None and author==None and amount==None:
        cur.execute('UPDATE books SET title = ? WHERE id = ? ', (title, id))
    elif author!=None and title==None and amount==None:
        cur.execute('UPDATE books SET author = ? WHERE id = ?', (author, id))
    elif amount!=None and title==None and author==None:
        cur.execute('UPDATE books SET amount = ? WHERE id = ?', (amount, id))
    elif amount!=None and title!=None and author==None:
        cur.execute('UPDATE books SET amount = ?, title = ? WHERE id = ?', (amount, title, id))
    elif amount!=None and title==None and author!=None:
        cur.execute('UPDATE books SET amount = ?, author = ? WHERE id = ?', (amount, author, id))
    elif amount==None and title!=None and author!=None:
        cur.execute('UPDATE books SET author = ?, title = ? WHERE id = ?', (author, title, id))
    elif amount!=None and title!=None and author!=None:
        cur.execute('UPDATE books SET amount = ?, author = ?, title = ? WHERE id = ?', (amount, author, title, id))
    close_connection(con)

def retrieve_book(name, id):
    con = connect_to_db()
    cur = con.cursor()
    cur.execute('UPDATE books SET amount= amount -1 WHERE id = ? AND amount != 0', (id,))
    cur.execute('SELECT title FROM books WHERE id = ?', (id,))
    book = cur.fetchall()
    try:
        book = book[0]
        book = book[0]
        cur.execute('INSERT INTO students (name, issued_book) VALUES (?,?)', (name, book))
        close_connection(con)
        return book
    except:
        close_connection(con)
        return 0


def close_connection(con):
    con.commit()
    con.close()