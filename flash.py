"""
Flashcard model
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Flashcard(Base):
    """
    Flashcard type object. Contains a title, a content (what's written on it) and a date when it was
    created. Aditionally, the flashcard can be marked as done.

    Properties:
        id: int
            Unique identifier of the flashcard on the database
        title: str
            Title of the flashcard
        content: str
            Content of the flashcard
        created_at: datetime
            When the flashcard was written
        is_checked: bool
            If the flashcard is marked as done
    """
    __tablename__ = 'flashcards'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    is_checked = Column(Boolean)

    def __str__(self):
        ttl = f'{self.id} - {self.title} {"(Done)" if self.is_checked else ""}'
        date = self.created_at.strftime('%b %d %Y')
        return f'{ttl}\n{date}\n\n{self.content}'
