from typing import Optional, List

from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException, status

import models
from crud.base import CRUDBase
from models.book import Book


class CRUDBook(CRUDBase):
    """
    CRUD book with methods to Create, Read, Update, Delete (CRUD).
    """

    def create(self,
               db: Session,
               obj_in: dict,
               authors: List[models.Author] = None) -> models.Book:
        db_new_book = Book(**obj_in)
        db_new_book.authors = authors
        db.add(db_new_book)
        db.commit()
        db.refresh(db_new_book)
        return db_new_book

    def update(
            self,
            db: Session,
            db_obj: models.Book,
            obj_in: dict,
            authors: List[models.Author] = None
    ) -> models.Book:
        obj_data = jsonable_encoder(db_obj)
        for field in obj_data:
            if field in obj_in:
                setattr(db_obj, field, obj_in[field])
        db_obj.authors = authors
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_name(
            self,
            db: Session,
            book_name: str
    ) -> Optional[Book]:
        return db.query(Book).filter(Book.name == book_name).first()

    def pass_book_name_or_400(
            self,
            new_book_name: str,
            db: Session,
            db_book: Book = None,
    ) -> None:
        exist_book = self.get_by_name(db=db, book_name=new_book_name)
        if not exist_book and not db_book:
            return
        elif db_book and exist_book and db_book.id == exist_book.id:
            return
        elif not exist_book:
            return
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'The author with name={new_book_name} already exists in the system'
        )


crud_book = CRUDBook(Book)
