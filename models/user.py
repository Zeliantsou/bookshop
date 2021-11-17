from typing import TYPE_CHECKING
from datetime import date

from sqlalchemy import Column, Boolean, Integer, String, Text, Date
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from models.book import Book


class User(Base):
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    name = Column(String, index=True, unique=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    books = relationship('Book', back_populates='user')
