import sqlite3
import tables

def connect_to_db():
    con = sqlite3.connect('lms.db')
    return con

def close_connection(con):
    con.commit()
    con.close()

def add_book(title, author, amount):
    con = connect_to_db()
    cur = con.cursor()
    try:
        cur.execute('INSERT INTO books (title, author, amount) VALUES (?,?,?)',(title, author, amount))
    except:
        print('The book already exists.')
    close_connection(con)

def add_student(name, id):
    con = connect_to_db()
    cur = con.cursor()
    try:
        cur.execute('INSERT INTO students (name, id) VALUES (?, ?)',(name, id))
    except:
        print('ID already registered.')
    close_connection(con)

def issue_book(sid, bid):
    con = connect_to_db()
    cur = con.cursor()
    cur.execute('SELECT * FROM lending_record WHERE student_id = ?', (sid,))
    repeated_id = cur.fetchall()
    cur.execute('SELECT name FROM students WHERE id = ?', (sid,))
    rows = cur.fetchall()
    if not rows:
        print('No Student with Such ID Registered!!!')
        close_connection(con)
        return 0
    elif repeated_id:
        print('One Student can Lend Only One Book!!!')
        close_connection(con)
        return 0
    else:
        cur.execute('SELECT title FROM books WHERE id = ? AND amount > 0', (bid,))
        book = cur.fetchall()
        try:
            book = book[0]
            book = book[0]
            cur.execute('INSERT INTO lending_record (student_id, issued_book_id) VALUES (?,?)', (sid, bid))
            cur.execute('UPDATE books SET amount= amount -1 WHERE id = ?', (bid,))
            close_connection(con)
            return book
        except:
            close_connection(con)
            print('Book is Not Available Right Now!!!')
            return 0

def return_book(sid):
    con = connect_to_db()
    cur = con.cursor()
    cur.execute('SELECT issued_book_id FROM lending_record WHERE student_id = ?', (sid,))
    rows = cur.fetchall()
    if not rows:
        print ('Book is not issued to the student...')
        close_connection(con)
        return
    else:
        bid = rows[0]
        bid = bid[0] 
        cur.execute('UPDATE books SET amount = amount + 1 WHERE id = ?', (bid,))
        cur.execute('DELETE FROM lending_record WHERE student_id = ?', (sid,))
        print("Book is Returned!!!")
    close_connection(con)

def remove_student(sid, set):
    con = connect_to_db()
    cur = con.cursor()
    cur.execute('SELECT id FROM lending_record WHERE student_id = ?', (sid,))
    rows = cur.fetchall()
    if not rows or set == 1:
        cur.execute('DELETE FROM students WHERE id = ?', (sid,))
        cur.execute('DELETE FROM lending_record WHERE student_id = ?', (sid,))
    else:
        close_connection(con)
        return 1
    close_connection(con)

def remove_book(bid, set):
    con = connect_to_db()
    cur = con.cursor()
    cur.execute('SELECT id FROM lending_record WHERE issued_book_id = ?', (bid,))
    rows = cur.fetchall()
    if not rows or set == 1:
        cur.execute('DELETE FROM books WHERE id = ?', (bid,))
        cur.execute('DELETE FROM lending_record WHERE issued_book_id = ?', (bid,))
    else:
        close_connection(con)
        return 1
    close_connection(con)

def update_book(title, author, amount, id):
    con = connect_to_db()
    cur = con.cursor()
    cur.execute('SELECT * FROM lending_record WHERE id = ?', (id,))
    rows = cur.fetchall()
    cur.execute('SELECT * FROM books WHERE id = ?', (id,))
    book_exists = cur.fetchall()
    if not rows and book_exists:
        if title==None and author==None and amount==None:
            print('Please give a value to be Updated. Try: py index.py admin update-book --a modified_author --t modified_title --n modified_amount')
        elif title!=None and author==None and amount==None:
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
        print('Updated!!!')
    else:
        print('Sorry! Either Book does not Exist Or it is Issued.')
    close_connection(con)

def view_student(sid, name):
    con = connect_to_db()
    cur = con.cursor()
    if sid and not name:
        cur.execute('SELECT * FROM students WHERE id = ?', (sid,))
    elif not sid and name:
        cur.execute('SELECT * FROM students WHERE name = ?', (name,))
    elif sid and name:
        cur.execute('SELECT * FROM students WHERE id = ? and name = ?', (sid, name))
    elif not sid and not name:
        cur.execute('SELECT * FROM students')
    rows = cur.fetchall()
    column_names = [column[0] for column in cur.description]
    result_rows = [column_names] + rows
    close_connection(con)
    return result_rows

def search_book(title, author, id):
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
    column_names = [column[0] for column in cur.description]
    result_rows = [column_names] + rows
    close_connection(con)
    return result_rows

def view_record(sid, bid):
    con = connect_to_db()
    cur = con.cursor()
    if not sid and bid:
        cur.execute('SELECT students.id AS student_id, students.name, books.id AS book_id, books.title, books.author, books.amount FROM lending_record JOIN books ON lending_record.issued_book_id = books.id JOIN students ON lending_record.student_id = students.id WHERE issued_book_id = ?', (bid,))
    elif not bid and sid:
        cur.execute('SELECT students.id AS student_id, students.name, books.id AS book_id, books.title, books.author, books.amount FROM lending_record JOIN books ON lending_record.issued_book_id = books.id JOIN students ON lending_record.student_id = students.id WHERE student_id = ?', (sid,))
    elif bid and sid:
        cur.execute('SELECT students.id AS student_id, students.name, books.id AS book_id, books.title, books.author, books.amount FROM lending_record JOIN books ON lending_record.issued_book_id = books.id JOIN students ON lending_record.student_id = students.id WHERE issued_book_id = ? AND student_id = ?', (bid, sid))
    elif not bid and not sid:
        cur.execute('SELECT students.id AS student_id, students.name, books.id AS book_id, books.title, books.author, books.amount FROM lending_record JOIN books ON lending_record.issued_book_id = books.id JOIN students ON lending_record.student_id = students.id')
    rows = cur.fetchall()
    column_names = [column[0] for column in cur.description]
    result_rows = [column_names] + rows
    close_connection(con)
    return result_rows


def my_book(sid):
    con = connect_to_db()
    cur = con.cursor()
    cur.execute('SELECT books.id, books.title  FROM lending_record JOIN books ON lending_record.issued_book_id = books.id WHERE student_id = ?', (sid,))
    rows = cur.fetchall()
    column_names = [column[0] for column in cur.description]
    result_rows = [column_names] + rows
    close_connection(con)
    return result_rows
