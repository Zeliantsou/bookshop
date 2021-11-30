from fastapi import HTTPException, status
from jose import jwt
from sqlalchemy.orm import Session

import crud
from core import security
from core.config import settings
import schemas


def create_access_token(user_id: int) -> str:
    """
    Create access token.
    """
    return security.create_token(user_id, settings.ACCESS_TOKEN_EXPIRE_MINUTES)


def create_refresh_token(user_id: int) -> str:
    """
    Create refresh token.
    """
    return security.create_token(user_id, settings.REFRESH_TOKEN_EXPIRE_MINUTES)


def generate_tokens(user_id: id) -> dict:
    """
    Generate access and refresh tokens.
    """
    return {
        "access_token": create_access_token(user_id),
        "refresh_token": create_refresh_token(user_id),
    }


def login_tokens(
        creds: schemas.UserLoginSchema,
        db: Session
) -> dict:
    """
    Login an user.
    """
    creds = creds.dict()
    user = crud.crud_user.authenticate(db, **creds)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Incorrect email or password'
        )
    elif not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='User is not active'
        )
    return generate_tokens(user.id)


def get_token_data(token: str) -> schemas.TokenPayload:
    """
    Get data from token.
    """
    try:
        payload = jwt.decode(
            token=token,
            key=settings.SECRET_KEY,
            algorithms=[security.ALGORITHM]
        )
        token_data = schemas.TokenPayload(**payload)
    except (jwt.JWTError, ValueError):
        HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Could not validate credentials'
        )
    return token_data


def refresh_tokes(db: Session, refresh_token: str) -> dict:
    """
    refresh access and refresh tokens.
    """
    token_data = get_token_data(refresh_token)
    user = crud.crud_user.get(db=db, id=token_data.sub)
    if not user:
        HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found'
        )
    return generate_tokens(user.id)
