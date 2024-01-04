import click

@click.command()
@click.option('--author', '--a', prompt='Author of the Book')
@click.option('--title', '--t', prompt='Title of Book: ')
@click.option('--amount', '--n', prompt='Total no. of Book: ')
def add_book(author, title, amount):
    """Add a Book"""
    click.echo(f"Book: {title}!")
    click.echo(f"Author: {author}!")
    click.echo(f"No. of Copies: {amount}!")

if __name__ == '__main__':
    add_book()