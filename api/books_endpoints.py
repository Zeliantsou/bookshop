from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models
import schemas
import services
from api.deps import get_db, get_current_user

router = APIRouter()


@router.post('/', response_model=schemas.BookBaseSchema)
def create_book(
        *,
        book_in: schemas.BookCreateUpdateSchema,
        db: Session = Depends(get_db),
        current_user: models.User = Depends(get_current_user),
) -> models.Book:
    """
    Create a book.
    """
    return services.book_services.create_book(
        book_in=book_in,
        db=db,
        current_user=current_user
    )


@router.patch('/{book_id}', response_model=schemas.BookBaseSchema)
def update_book(
        book_id: int,
        book_in: schemas.BookCreateUpdateSchema,
        db: Session = Depends(get_db),
        current_user: models.User = Depends(get_current_user)
) -> models.Book:
    """
    Update a book.
    """
    return services.book_services.update_book(
        book_id=book_id,
        book_in=book_in,
        db=db,
        current_user=current_user
    )


@router.get('/{book_id}', response_model=schemas.BookBaseSchema)
def get_book(
        book_id: int,
        db: Session = Depends(get_db)
) -> Optional[models.Book]:
    """
    Get a book by id.
    """
    return services.book_services.get_book(
        book_id=book_id,
        db=db
    )


@router.get('/', response_model=List[schemas.BookBaseSchema])
def get_book_list(
    db: Session = Depends(get_db),
    skip: int = None,
    limit: int = None,
) -> List[models.Book]:
    """
    Get list of books.
    """
    return services.book_services.get_book_list(
        db=db,
        skip=skip,
        limit=limit
    )


@router.delete('/{book_id}', response_model=schemas.BookBaseSchema)
def delete_book(
        book_id: int,
        db: Session = Depends(get_db),
        current_user: models.User = Depends(get_current_user)
) -> models.Book:
    """
    Delete a book.
    """
    return services.book_services.delete_book(
        book_id=book_id,
        db=db,
        current_user=current_user
    )
