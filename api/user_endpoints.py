from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models
import schemas
import services
from api.deps import get_db, get_current_user

router = APIRouter()


@router.post('/', response_model=schemas.UserBaseSchema)
def create_user(
    *,
    user_in: schemas.UserCreateSchema,
    db: Session = Depends(get_db),
) -> models.User:
    return services.user_services.create_user(user_in=user_in, db=db)


@router.patch('/update-user/{user_id}', response_model=schemas.UserBaseSchema)
def update_user(
    *,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
    user_in: schemas.UserUpdateSchema,
    user_id: int
) -> models.User:
    return services.user_services.update_user(
        db=db,
        current_user=current_user,
        user_in=user_in,
        user_id=user_id
    )


@router.get('/{user_id}', response_model=schemas.UserBaseSchema)
def get_user(
        user_id: int,
        db: Session = Depends(get_db),
        current_user: models.User = Depends(get_current_user)
) -> Optional[models.User]:
    user = services.user_services.get_user(
        user_id=user_id,
        db=db,
        current_user=current_user
    )
    return user


@router.get('/list/', response_model=List[schemas.UserBaseSchema])
def get_user_list(
        limit: int = None,
        skip: int = None,
        db: Session = Depends(get_db),
        current_user: models.User = Depends(get_current_user)
) -> [List[models.User]]:
    user_list = services.user_services.get_user_list(
        limit=limit,
        skip=skip,
        db=db,
        current_user=current_user
    )
    return user_list


@router.delete('/{user_id}', response_model=schemas.UserBaseSchema)
def delete_user(
        user_id: int,
        db: Session = Depends(get_db),
        current_user: models.User = Depends(get_current_user)
) -> models.User:
    return services.user_services.delete_user(
        user_id=user_id,
        db=db,
        current_user=current_user
    )
