from typing import Optional
from datetime import date

from pydantic import BaseModel


class AuthorBaseSchema(BaseModel):
    """
    Base schema for author.
    """
    name: str
    description: Optional[str]
    birthday: date

    class Config:
        orm_mode = True


class AuthorCreateUpdateSchema(AuthorBaseSchema):
    """
    Schema for creating and updating author.
    """
    pass


class AuthorRetrieveListSchema(AuthorBaseSchema):
    """
    Schema for retrieving list of authors or certain author.
    """
    id: int
