from typing import Optional
from datetime import date

from pydantic import BaseModel


class AuthorBaseSchema(BaseModel):
    name: str
    description: Optional[str]
    birthday: date

    class Config:
        orm_mode = True


class AuthorCreateUpdateSchema(AuthorBaseSchema):
    pass


class AuthorRetrieveListSchema(AuthorBaseSchema):
    id: int
