from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from api.deps import get_db, get_current_user

router = APIRouter()


@router.post('/', response_model=schemas.UserBaseSchema)
def create_user(
    *,
    user_in: schemas.UserCreateSchema,
    db: Session = Depends(get_db),
) -> Any:
    user = crud.crud_user.get_by_name(db, name=user_in.name)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = crud.crud_user.create(db, obj_in=user_in)
    return user
