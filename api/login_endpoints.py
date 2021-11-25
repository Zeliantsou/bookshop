from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import services
import models
import schemas
from api.deps import get_db, get_current_user

router = APIRouter()


@router.post('/login/tokens', response_model=schemas.Token)
def login_tokens(
    creds: schemas.UserLoginSchema,
    db: Session = Depends(get_db),
) -> dict:
    return services.login_services.login_tokens(creds=creds, db=db)


@router.post('/login/test-token', response_model=schemas.UserBaseSchema)
def test_token(current_user: models.User = Depends(get_current_user)) -> models.User:
    return current_user


@router.post('/login/refresh-tokens', response_model=schemas.Token)
def refresh_tokens(
        refresh_token: str,
        db: Session = Depends(get_db)
) -> dict:
    refreshed_tokens = services.login_services.refresh_tokes(db=db, refresh_token=refresh_token)
    return refreshed_tokens
