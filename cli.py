"""
Command line interface
"""

import click

import control


# noinspection PyMissingOrEmptyDocstring
@click.group()
def cli(): pass


@cli.command()
def list_all():
    """
    List every flashcard
    """
    for fid, name in control.list_flashcards():
        print(f'{fid} - {name}')


@cli.command()
@click.argument('title')
@click.argument('content')
def add_flashcard(title: str, content: str):
    """
    Adds a new flashcard

    \b
    :param title: Flashcard title
    :param content: Flashcard contents
    """
    control.add_flashcard(title, content)
    print('Flashcard has been added')


@cli.command()
@click.argument('string')
def title_search(string: str):
    """
    Looks for a matching title

    :param string: Search string
    """
    for fid, title in control.title_search(string):
        print(f'{fid} - {title}')


@cli.command()
@click.argument('flashcard_id')
def print_flashcard(flashcard_id):
    """
    Prints the content of a flashcard

    \b
    :param flashcard_id: ID of the flashcard to print
    """
    print(control.get_flashcard(flashcard_id))


@cli.command()
@click.argument('flashcard_id')
def delete_flashcard(flashcard_id):
    """
    Deletes a flashcard

    \b
    :param flashcard_id: ID of the flashcard to delete
    """
    control.delete_flashcard(flashcard_id)
    print('The flashcard has been deleted')


@cli.command()
@click.argument('flashcard_id')
def check_flashcard(flashcard_id):
    """
    Marks the flashcard as (not) done, based on the previous state.

    \b
    :param flashcard_id: ID of the flashcard to mark.
    """
    if control.check_flashcard(flashcard_id):
        print('Flashcard marked as done')
    else:
        print('Flashcard marked as not done')


if __name__ == '__main__':
    cli()
