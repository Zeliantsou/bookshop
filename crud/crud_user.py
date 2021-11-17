from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from base import CRUDBase
from models.user import User
from schemas.user import UserCreateSchema, UserUpdateSchema
from core.security import  get_password_hash, verify_password


class CRUDUser(CRUDBase[User, UserCreateSchema, UserUpdateSchema]):

    def get_by_name(self, db: Session, *, name: str) -> Optional[User]:
        return db.query(User).filter(self.name == name).first()

    def create(self, db: Session, obj_in: UserCreateSchema) -> User:
        obj_in_data = obj_in.dict()
        obj_in_data['hashed_password'] = get_password_hash(obj_in_data.pop('password'))
        db_obj = User(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
            self,
            db: Session,
            *,
            db_obj: User,
            obj_in: Union[UserUpdateSchema, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data['password']:
            update_data['hashed_password'] = get_password_hash(update_data.pop('password'))
        super().update(db, db_obj=db_obj, obj_in=update_data)

    def authenticate(self, db: Session, *, name: str, password: str) -> Optional[User]:
        user = self.get_by_name(db, name=name)
        if user and verify_password(password, user.hashed_password):
            return user
        return None


crud_user = CRUDUser(User)