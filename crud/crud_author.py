from typing import Optional

from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from crud.base import CRUDBase
from models.author import Author


class CRUDAuthor(CRUDBase):
    """
    CRUD author with default methods to Create, Read, Update, Delete (CRUD).
    """
    def get_by_name(
            self,
            db: Session,
            author_name: str
    ) -> Optional[Author]:
        return db.query(Author).filter(Author.name == author_name).first()

    def pass_author_name_or_400(
            self,
            new_author_name: str,
            db: Session,
            db_author: Author = None,
    ) -> None:
        exist_author = self.get_by_name(db=db, author_name=new_author_name)
        if not exist_author and not db_author:
            return
        elif db_author and exist_author and db_author.id == exist_author.id:
            return
        elif not exist_author:
            return
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'The author with name={new_author_name} already exists in the system'
        )


crud_author = CRUDAuthor(Author)
