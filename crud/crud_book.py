from crud.base import CRUDBase
from models.book import Book


class CRUDBook(CRUDBase):
    pass


crud_book = CRUDBook(Book)
