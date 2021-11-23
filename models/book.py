from typing import TYPE_CHECKING
from datetime import date

from sqlalchemy import Column, ForeignKey, String, Integer, Date, Numeric
from sqlalchemy.orm import relationship, backref

from db.base_class import Base
from models.author_book import author_book

if TYPE_CHECKING:
    from models.user import User
    from models.author import Author


class Book(Base):
    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    price = Column(Numeric)
    added = Column(Date, default=date.today)
    pages = Column(Integer)
    authors = relationship('Author', secondary=author_book, backref=backref('books', lazy='dynamic'))
    owner_id = Column(Integer, ForeignKey('user.id'))
    owner = relationship('User', back_populates='books')
