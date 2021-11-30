from typing import Optional, List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

import crud
import models
import schemas


def check_exists_user_name(user_name: str, db: Session) -> None:
    """
    Check an existing user by name.
    """
    if crud.crud_user.get_by_name(name=user_name, db=db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='The user with this username already exists in the system'
        )


def check_exists_user_email(user_email: str, db: Session) -> None:
    """
    Check an existing user by email.
    """
    if crud.crud_user.get_by_email(email=user_email, db=db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='The user with this email already exists in the system'
        )


def create_user(
        user_in: schemas.UserCreateSchema,
        db: Session
) -> models.User:
    """
    Create an user.
    """
    check_exists_user_name(user_name=user_in.name, db=db)
    check_exists_user_email(user_email=user_in.email, db=db)
    return crud.crud_user.create(db=db, obj_in=user_in)


def update_user(
        db: Session,
        current_user: models.User,
        user_in: schemas.UserUpdateSchema,
        user_id: int) -> models.User:
    """
    Update an user.
    """
    crud.crud_user.allow_or_403(user=current_user, check_owner_id=user_id)
    mutable_user = crud.crud_user.get_or_404(db=db, id=user_id)
    if mutable_user.name != user_in.name:
        check_exists_user_name(user_name=user_in.name, db=db)
    if mutable_user.email != user_in.email:
        check_exists_user_email(user_email=user_in.email, db=db)
    return crud.crud_user.update(db=db, db_obj=mutable_user, obj_in=user_in)


def get_user(
        user_id: int,
        db: Session,
        current_user: models.User
) -> Optional[models.User]:
    """
    Get user by id.
    """
    crud.crud_user.allow_or_403(user=current_user, check_owner_id=user_id)
    return crud.crud_user.get_or_404(db=db, id=user_id)


def get_user_list(
        limit: int,
        skip: int,
        db: Session,
        current_user: models.User
) -> List[models.User]:
    """
    Get list of users.
    """
    if current_user.is_superuser:
        return crud.crud_user.get_multi(db=db, skip=skip, limit=limit)
    return [current_user]


def delete_user(
        user_id: int,
        db: Session,
        current_user: models.User
) -> models.User:
    """
    Delete an user.
    """
    crud.crud_user.allow_or_403(user=current_user, check_owner_id=user_id)
    return crud.crud_user.remove(db=db, id=user_id)
