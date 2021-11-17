from typing import List, Optional
from decimal import Decimal
from datetime import date

from pydantic import BaseModel

from schemas.author import AuthorBaseSchema


class BookBaseSchema(BaseModel):
    name: str
    description: Optional[str]
    price: Decimal
    added: date = date.today()  # нужно ли вызывать today?
    pages: int
    authors: List[AuthorBaseSchema]


class BookCreateUpdateSchemaForAdmin(BookBaseSchema):
    owner_id: Optional[int]


class BookRetrieveListSchemaForAdmin(BookBaseSchema):
    id: int
    owner_id: Optional[int]


class BookRetrieveListSchema(BookBaseSchema):
    owner_id: Optional[int]  # поле, чтобы выводилось не id, a name user
