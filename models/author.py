from typing import TYPE_CHECKING
from datetime import date

from sqlalchemy import Column, Integer, String, Text, Date
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from models.book import Book


class Author(Base):
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, index=True, unique=True)
    description = Column(Text(length=500))
    birthday = Column(Date, default=date.today())
