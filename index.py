import click
import db

@click.command()
@click.option('--author', '--a', prompt='Author of the Book')
@click.option('--title', '--t', prompt='Title of Book: ')
@click.option('--amount', '--n', prompt='Total no. of Book: ')
def add_book(author, title, amount):
    """Add a Book"""
    db.insert_book(author, title, amount)
    
    data = db.fetch_book()

    # Print the fetched data
    print("Data in the table:")
    for row in data:
        print(row)

if __name__ == '__main__':
    add_book()