from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from api.deps import get_db, get_current_user
from core import security
from core.config import settings

router = APIRouter()


@router.post('/login/access-token', response_model=schemas.Token)
def login_access_token(
    creds: schemas.UserLoginSchema,
    db: Session = Depends(get_db),
) -> Any:
    user = crud.crud_user.authenticate(db, **creds)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect name or password")
    # elif not user.is_active:
    #     raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }


@router.post('/login/test-token', response_model=schemas.UserBaseSchema)
def test_token(current_user: models.User = Depends(get_current_user)) -> Any:
    return current_user
