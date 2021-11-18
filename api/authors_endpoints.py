from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import schemas
import models
import crud
from api.deps import get_db, get_current_user

router = APIRouter()


def get_response_model(current_user: models.User):
    if current_user.is_superuser:
        return List[schemas.AuthorRetrieveListSchema]
    return List[schemas.AuthorBaseSchema]


@router.get('/', response_model=get_response_model(Depends(get_current_user)))  # только Depends могу передать?
def get_author_list(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    return crud.crud_author.get_multi(db, skip=skip, limit=limit)


@router.post('/', response_model=schemas.AuthorCreateUpdateSchema)
def create_author(
        *,
        db: Session = Depends(get_db),
        author_in = schemas.AuthorCreateUpdateSchema,
        current_user: models.User = Depends(get_current_user)
) -> Any:
    if current_user.is_superuser:
        return crud.crud_author.create(db=db, obj_in=author_in)
    raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Current user can't create a book",
        )
