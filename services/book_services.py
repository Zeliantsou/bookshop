from typing import List, Optional, Set

from sqlalchemy.orm import Session

import crud
import models
import schemas


def generate_author_list_for_book(db: Session, author_ids: Set[int]) -> List[models.Author]:
    author_list_add = []
    for author_id in author_ids:
        author_add = crud.crud_author.get_or_404(db=db, id=author_id)
        author_list_add.append(author_add)
    return author_list_add


def create_book(
        book_in: schemas.BookCreateUpdateSchema,
        db: Session,
        current_user: models.User
) -> models.Book:
    """
    Create a book.
    """
    crud.crud_user.allow_or_403(user=current_user)
    crud.crud_user.get_or_404(db=db, id=book_in.owner_id)
    crud.crud_book.pass_book_name_or_400(
        new_book_name=book_in.name,
        db=db
    )
    book_in = dict(book_in)
    author_ids = set(book_in.pop('author_ids'))
    return crud.crud_book.create(
        db=db,
        obj_in=book_in,
        authors=generate_author_list_for_book(db=db, author_ids=author_ids)
    )


def update_book(
        book_id: int,
        book_in: schemas.BookCreateUpdateSchema,
        db: Session,
        current_user: models.User
) -> models.Book:
    """
    Update a book.
    """
    crud.crud_user.allow_or_403(user=current_user)
    crud.crud_user.get_or_404(db=db, id=book_in.owner_id)
    mutable_book = crud.crud_book.get_or_404(db=db, id=book_id)
    crud.crud_book.pass_book_name_or_400(
        db_book=mutable_book,
        new_book_name=book_in.name,
        db=db
    )
    book_in = dict(book_in)
    author_ids = set(book_in.pop('author_ids'))
    return crud.crud_book.update(
        db=db,
        db_obj=mutable_book,
        obj_in=book_in,
        authors=generate_author_list_for_book(db=db, author_ids=author_ids)
    )


def get_book(db: Session, book_id: int) -> Optional[models.Book]:
    """
    Get book by id.
    """
    return crud.crud_book.get_or_404(db=db, id=book_id)


def get_book_list(db: Session, skip: int, limit: int) -> List[models.Book]:
    """
    Get list of books.
    """
    return crud.crud_book.get_multi(db=db, skip=skip, limit=limit)


def delete_book(
        book_id: int,
        db: Session,
        current_user: models.User
) -> models.Book:
    """
    Delete a book.
    """
    crud.crud_user.allow_or_403(user=current_user)
    crud.crud_book.get_or_404(db=db, id=book_id)
    return crud.crud_book.remove(db=db, id=book_id)
