from typing import TYPE_CHECKING
from datetime import date

from sqlalchemy import Column, ForeignKey, String, Integer, Text, Date, Numeric
from sqlalchemy.orm import relationship, backref

from db.base_class import Base


if TYPE_CHECKING:
    from models.user import User
    from models.author import Author


class AuthorBook(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    author_id = Column(Integer, ForeignKey('author.id'))
    book_id = Column(Integer, ForeignKey('book.id'))

    def __tablename__(cls):
        return 'author_book'


class Book(Base):
    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True)  # зачем в Base указывать id?
    name = Column(String, unique=True, index=True)
    description = Column(Text(length=500))
    price = Column(Numeric)
    added = Column(Date, default=date.today)
    pages = Column(Integer)
    authors = relationship('Author', secondary='author_book', backref=backref('books', lazy='dynamic'))
    owner_id = Column(Integer, ForeignKey('user.id'))
    owner = relationship('User', back_populates='books')
