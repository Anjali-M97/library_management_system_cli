import click
import db

@click.group()
def cli():
    pass

@cli.command()
@click.option('--author', '--a', prompt='Author of the Book')
@click.option('--title', '--t', prompt='Title of Book: ')
@click.option('--amount', '--n', prompt='Total no. of Book: ')
def add_book(author, title, amount):
    """Add a Book"""
    db.insert_book(title, author, amount)

@cli.command()
def view_books():
    data = db.fetch_book()

    # Print the fetched data
    print("Data in the table:")
    for row in data:
        print(row)

@cli.command()
@click.option('--author', '--a', help='Author to Search', default=None )
@click.option('--title', '--t', help='Book to Search', default=None)
def search_book(author, title):
    """Search a Book"""
    data = db.find_book(title, author)

    print("Data in the table:")
    for row in data:
        print(row)

@cli.command()
@click.option('--author', '--a', prompt='Author of the Book')
@click.option('--title', '--t', prompt='Title of Book: ')
def remove_book(author, title):
    """Remove a Book"""
    db.delete_book(title, author)

if __name__ == '__main__':
    cli()