import click
import db

@click.group()
def cli():
    pass

@cli.group()
def admin():
    pass

@admin.command()
@click.option('--author', '--a', prompt='Author of the Book')
@click.option('--title', '--t', prompt='Title of Book: ')
@click.option('--amount', '--n', prompt='Total no. of Book: ')
def add_book(author, title, amount):
    """Add a Book"""
    db.insert_book(title, author, amount)

@admin.command()
def lend_record():
    '''View Lend Record'''
    data = db.view_record()
    
    print("Data in the table:")
    for row in data:
        print(row)

@admin.command()
def view_books():
    data = db.fetch_book()

    # Print the fetched data
    print("Data in the table:")
    for row in data:
        print(row)

@admin.command()
@click.option('--author', '--a', help='Author to Search', default=None )
@click.option('--title', '--t', help='Book to Search', default=None)
@click.option('--id', help='Identification Number', default=None)
def search_book(author, title, id):
    """Search a Book"""
    data = db.find_book(title, author, id)

    print("Data in the table:")
    for row in data:
        print(row)

@admin.command()
@click.option('--id', prompt='Enter ID of the Book')
def remove_book(id):
    """Remove a Book"""
    db.delete_book(id)

@admin.command()
@click.option('--author', '--a', help='Author to Search', default=None )
@click.option('--title', '--t', help='Book to Search', default=None)
@click.option('--amount', '--n', help='No. of Books Available', default=None)
@click.option('--id', prompt='Identification Number')
def update_book(author, title, amount, id):
    """Update Record Data"""
    db.update_book(title, author, amount, id)

@admin.command()
@click.option('--name', '--nm', prompt= 'Enter your Name')
@click.option('--id', prompt='ID of Book you Want')
def retrieve(name, id):
    '''Issue a Book'''
    book= db.retrieve_book(name, id)
    click.echo(f'{book} has been issued to you!')

@admin.command()
@click.option('--sname', '--nm', prompt= 'Enter Students Name')
@click.option('--id', prompt='ID of Book you Want to Return')
def return_book(sname, id):
    '''Return a Book'''
    db.return_book(sname, id)

@cli.group()
def students():
    pass

@students.command()
@click.option('--author', '--a', help='Author to Search', default=None )
@click.option('--title', '--t', help='Book to Search', default=None)
@click.option('--id', help='Identification Number', default=None)
def search_book(author, title, id):
    """Search a Book"""
    data = db.find_book(title, author, id)

    print("Data in the table:")
    for row in data:
        print(row)

if __name__ == '__main__':
    cli()