"""
Flashcard model
"""
from datetime import datetime
from typing import Optional

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Flashcard(Base):
    """
    TODO: Write this
    """
    __tablename__ = 'flashcards'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    date = Column(DateTime)
    is_checked = Column(Boolean)

    def __init__(self, title: str, content: str, date: Optional[datetime] = None):
        self.title = title
        self.content = content
        if date is None:
            date = datetime.today()
        self.date = date
        self.is_checked = False

    def __str__(self):
        ttl = f'{self.id} - {self.title} {"(Done)" if self.is_checked else ""}'
        date = self.date.strftime('%b %d %Y')
        return f'{ttl}\n{date}\n\n{self.content}'

    def check(self):
        """
        Changes between checked and unchecked
        """
        if self.is_checked:
            self.is_checked = False
        else:
            self.is_checked = True
