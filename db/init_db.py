from sqlalchemy.orm import Session

from core.config import settings
from schemas.user import CreateFirstSuperuserSchema
from crud.crud_user import crud_user


def init_db(db: Session) -> None:
    """
    Create the first superuser if it does not exist.
    """
    user = crud_user.get_by_name(db, name=settings.FIRST_SUPERUSER)
    if not user:
        user_in = CreateFirstSuperuserSchema(
            name=settings.FIRST_SUPERUSER,
            email=settings.FIRST_SUPERUSER_EMAIL,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True
        )
        crud_user.create(db, obj_in=user_in)
