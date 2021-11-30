from typing import List, Optional
from decimal import Decimal
from datetime import date

from pydantic import BaseModel


class BookBaseSchema(BaseModel):
    """
    Base schema for book.
    """
    name: str
    description: Optional[str]
    price: Decimal
    added: date = date.today()
    pages: int

    class Config:
        orm_mode = True


class BookCreateUpdateSchema(BookBaseSchema):
    """
    Schema for creating and updating books.
    """
    owner_id: Optional[int]
    author_ids: List[int]


class BookRetrieveListSchemaForAdmin(BookBaseSchema):
    """
    Schema for retrieving list of book or certain book for superuser.
    """
    id: int
    owner_id: Optional[int]


class BookRetrieveListSchema(BookBaseSchema):
    """
    Schema for retrieving list of book or certain book for plain user.
    """
    owner_id: Optional[int]
