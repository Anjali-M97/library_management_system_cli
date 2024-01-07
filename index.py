import click
from functions import tabular_data
import db

@click.group()
def cli():
    '''Welcom to the Library...'''
    pass

@cli.group()
def admin():
    '''Admin Access'''
    pass

@admin.command()
@click.option('--author', '--a', prompt='Author of the Book')
@click.option('--title', '--t', prompt='Title of Book: ')
@click.option('--amount', '--n', prompt='Total no. of Book: ', type=click.IntRange(1, None))
def add_book(author, title, amount):
    """Add a Book"""
    db.add_book(title, author, amount)

@admin.command()
@click.option('--sname', '--nm', prompt='Name of the Student:')
@click.option('--id', prompt='ID of the Student: ', type=click.IntRange(1, None))
def add_student(sname, id):
    """Add a Student"""
    db.add_student(sname, id)

@admin.command()
@click.option('--sid', prompt= 'Enter Students ID:')
@click.option('--bid', prompt='ID of Book to Issue:')
def issue_book(sid, bid):
    '''Issue a Book'''
    book= db.issue_book(sid, bid)
    if book:
        click.echo(f'{book} has been issued!')

@admin.command()
@click.option('--sid', prompt= 'Students ID')
def return_book(sid):
    '''Return a Book'''
    db.return_book(sid)

@admin.command()
@click.option('--id', prompt='Enter ID of the Student:')
@click.option('--set', type=click.IntRange(0, 1), default = 0, help='Set the Value to 1 to delete student record even if a book is issued.')
def remove_student(id, set):
    """Remove a Student"""
    flag = db.remove_student(id, set)
    if flag:
        confirm = click.confirm('A book is issued to this student. Do you still want to delete?', default=False)
        if confirm:
            db.remove_student(id, 1)

@admin.command()
@click.option('--id', prompt='Enter ID of the Book:')
@click.option('--set', type=click.IntRange(0, 1), default = 0, help='Set the Value to 1 to delete book even if it is issued.')
def remove_book(id, set):
    """Remove a Book"""
    flag = db.remove_book(id, set)
    if flag:
        confirm = click.confirm('This book is issued to a student. Do you still want to delete?', default=False)
        if confirm:
            db.remove_book(id, 1)

@admin.command()
@click.option('--author', '--a', help='Update Author', default=None )
@click.option('--title', '--t', help='Update Title', default=None)
@click.option('--amount', '--n', help='Update No. of Books Available', default=None, type=click.IntRange(1, None))
@click.option('--id', prompt='Identification Number')
def update_book(author, title, amount, id):
    """Update Record Data"""
    db.update_book(title, author, amount, id)

@admin.command()
@click.option('--sid', help='Students ID:')
@click.option('--name', '--nm', help='Students Name: ')
def view_student(sid, name):
    '''View Students Record'''
    data = db.view_student(sid, name)
    print("Data in the table:")
    tabular_data(data)

@admin.command()
@click.option('--author', '--a', help='Author to Search', default=None )
@click.option('--title', '--t', help='Book to Search', default=None)
@click.option('--id', help='Identification Number', default=None)
def search_book(author, title, id):
    """Search Books"""
    data = db.search_book(title, author, id)
    print("Data in the table:")
    tabular_data(data)

@admin.command()
@click.option('--sid', help='ID of the Student')
@click.option('--bid', help='ID of the Book: ')
def view_record(sid, bid):
    '''View Lending Record'''
    data = db.view_record(sid, bid)
    print("Data in the table:")
    tabular_data(data)

    
@cli.group()
def students():
    '''Students Access'''
    pass

@students.command()
@click.option('--author', '--a', help='Author to Search', default=None )
@click.option('--title', '--t', help='Book to Search', default=None)
@click.option('--id', help='Identification Number of Book', default=None)
def search_book(author, title, id):
    """Search a Book"""
    data = db.search_book(title, author, id)
    print("Data in the table:")
    tabular_data(data)

@students.command()
@click.option('--sid', prompt='Your Id')
def my_book(sid):
    '''View the Book You Issued'''
    data = db.my_book(sid)
    print("Data in the table:")
    tabular_data(data)

if __name__ == '__main__':
    cli()