from sqlalchemy import Column, ForeignKey, Integer, Table

from db.base_class import Base


author_book = Table(
    'author_book',
    Base.metadata,
    Column('author_id', Integer(), ForeignKey('author.id')),
    Column('book_id', Integer(), ForeignKey('book.id'))
)
