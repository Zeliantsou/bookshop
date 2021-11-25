from typing import Generator

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, Header

from db.session import SessionLocal
import crud
import models
import services


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(
        db: Session = Depends(get_db),
        token: str = Header(None),
) -> models.User:
    token_data = services.login_services.get_token_data(token=token)
    user = crud.crud_user.get(db, id=token_data.sub)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found',
        )
    return user
