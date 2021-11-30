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
    """
    Create an user.
    """
    return services.user_services.create_user(user_in=user_in, db=db)


@router.patch('/{user_id}', response_model=schemas.UserBaseSchema)
def update_user(
    *,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
    user_in: schemas.UserUpdateSchema,
    user_id: int
) -> models.User:
    """
    Update an user.
    """
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
    """
    Get user by id.
    """
    return services.user_services.get_user(
        user_id=user_id,
        db=db,
        current_user=current_user
    )


@router.get('/', response_model=List[schemas.UserBaseSchema])
def get_user_list(
        limit: int = None,
        skip: int = None,
        db: Session = Depends(get_db),
        current_user: models.User = Depends(get_current_user)
) -> [List[models.User]]:
    """
    Get list of users.
    """
    return services.user_services.get_user_list(
        limit=limit,
        skip=skip,
        db=db,
        current_user=current_user
    )


@router.delete('/{user_id}', response_model=schemas.UserBaseSchema)
def delete_user(
        user_id: int,
        db: Session = Depends(get_db),
        current_user: models.User = Depends(get_current_user)
) -> models.User:
    """
    Delete an user.
    """
    return services.user_services.delete_user(
        user_id=user_id,
        db=db,
        current_user=current_user
    )
