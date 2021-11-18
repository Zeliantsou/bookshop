from sqlalchemy import Column, ForeignKey, Integer

from db.base_class import Base


class AuthorBook(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    author_id = Column(Integer, ForeignKey('author.id'))
    book_id = Column(Integer, ForeignKey('book.id'))

    def __tablename__(cls):
        return 'author_book'
