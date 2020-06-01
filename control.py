"""
Actions using the Flashcard class
"""
from datetime import datetime
from typing import Optional, List, Tuple

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from flash import Flashcard

engine = create_engine('sqlite:///flash.db', echo=False)
session = sessionmaker(bind=engine)()


def list_flashcards() -> List[Tuple[int, str]]:
    """
    :return: List every id and title of every flashcard in the db
    """
    flashcards = []
    for flashcard in session().query(Flashcard):
        flashcard.append(flashcard.id, flashcard.title)
    return flashcards


def add_flashcard(title: str, content: str, date: Optional[datetime] = None):
    """
    Adds a new flashcard to the db

    :param title: Flashcard title
    :param content: Content of the flashcard
    :param date: Optional argument. Date of the flashcard.
    """
    flashcard = Flashcard(title, content, date)
    session.add(flashcard)
    session.commit()


def title_search(string: str) -> List[Tuple[int, str]]:
    """
    Search for title matches on the db

    :param string: Title string to search
    :return: List with the id and title of matching flashcards
    """
    results = []
    for flashcard in session.query(Flashcard):
        if string.lower() in flashcard.title.lower():
            results.append((flashcard.id, flashcard.title))
    return results


def get_flashcard(flashcard_id) -> Flashcard:
    """
    :param flashcard_id: Database unique ID of the flashcard
    :return: Flashcard object with flashcard_id as ID
    """
    return session.query(Flashcard).get(flashcard_id)


def delete_flashcard(flashcard_id):
    """
    Deletes a flashcard in the db.

    :param flashcard_id: Flashcard ID to delete.
    """
    session.delete(get_flashcard(flashcard_id))
    session.commit()


def check_flashcard(flashcard_id):
    """
    Checks or unchecks a flashcard

    :param flashcard_id: Database unique ID of the flashcard to check
    :return: New status of the flashcard
    """
    flashcard = get_flashcard(flashcard_id)
    flashcard.check()
    return flashcard.is_done
