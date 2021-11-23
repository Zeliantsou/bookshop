from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import schemas
import models
import crud
from api.deps import get_db, get_current_user

router = APIRouter()


@router.get('/', response_model=List[schemas.AuthorRetrieveListSchema])
def get_author_list_admin(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    return crud.crud_author.get_multi(db, skip=skip, limit=limit)


@router.get('/', response_model=List[schemas.AuthorBaseSchema])
def get_author_list_user(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    return crud.crud_author.get_multi(db, skip=skip, limit=limit)


@router.post('/', response_model=schemas.AuthorCreateUpdateSchema)
def create_author(
        *,
        author_in: schemas.AuthorCreateUpdateSchema,
        db: Session = Depends(get_db),
        current_user: models.User = Depends(get_current_user),
) -> Any:
    if crud.crud_user.is_superuser(current_user):
        return crud.crud_author.create(db=db, obj_in=author_in)
    raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Current user can't create a book",
        )
