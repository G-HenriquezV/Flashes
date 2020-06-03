"""
Flashcard model
"""
from datetime import datetime

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
    created_at = Column(DateTime, default=datetime.now)
    is_checked = Column(Boolean)

    def __str__(self):
        ttl = f'{self.id} - {self.title} {"(Done)" if self.is_checked else ""}'
        date = self.created_at.strftime('%b %d %Y')
        return f'{ttl}\n{date}\n\n{self.content}'
