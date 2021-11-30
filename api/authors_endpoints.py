from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models
import schemas
import services
from api.deps import get_db, get_current_user

router = APIRouter()


@router.post('/', response_model=schemas.AuthorCreateUpdateSchema)
def create_author(
        *,
        author_in: schemas.AuthorCreateUpdateSchema,
        db: Session = Depends(get_db),
        current_user: models.User = Depends(get_current_user),
) -> models.Author:
    """
    Create an author.
    """
    return services.author_services.create_author(
        author_in=author_in,
        db=db,
        current_user=current_user
    )


@router.patch('/{author_id}', response_model=schemas.AuthorCreateUpdateSchema)
def update_author(
        author_id: int,
        author_in: schemas.AuthorCreateUpdateSchema,
        db: Session = Depends(get_db),
        current_user: models.User = Depends(get_current_user)
) -> models.Author:
    """
    Update an author.
    """
    return services.author_services.update_author(
        author_id=author_id,
        author_in=author_in,
        db=db,
        current_user=current_user
    )


@router.get('/{author_id}', response_model=schemas.AuthorRetrieveListSchema)
def get_author(
        author_id: int,
        db: Session = Depends(get_db)
) -> Optional[models.Author]:
    """
    Get an author by id.
    """
    return services.author_services.get_author(
        author_id=author_id,
        db=db
    )


@router.get('/', response_model=List[schemas.AuthorRetrieveListSchema])
def get_author_list(
    db: Session = Depends(get_db),
    skip: int = None,
    limit: int = None,
) -> List[models.Author]:
    """
    Get list of authors.
    """
    return services.author_services.get_author_list(
        db=db,
        skip=skip,
        limit=limit
    )


@router.delete('/{author_id}', response_model=schemas.AuthorBaseSchema)
def delete_author(
        author_id: int,
        db: Session = Depends(get_db),
        current_user: models.User = Depends(get_current_user)
) -> models.Author:
    """
    Delete an author.
    """
    return services.author_services.delete_author(
        author_id=author_id,
        db=db,
        current_user=current_user
    )
