from base import CRUDBase
from models.author import Author


class CRUDAuthor(CRUDBase):
    pass


crud_author = CRUDAuthor(Author)
