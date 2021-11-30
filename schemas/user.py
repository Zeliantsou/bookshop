from pydantic import BaseModel, EmailStr


class UserBaseSchema(BaseModel):
    """
    Base schema for user.
    """
    name: str
    email: EmailStr

    class Config:
        orm_mode = True


class UserCreateSchema(UserBaseSchema):
    """
    Schema for creating user.
    """
    password: str


class CreateFirstSuperuserSchema(UserCreateSchema):
    """
    Schema for creating the first superuser.
    """
    is_superuser: bool


class UserUpdateSchema(UserBaseSchema):
    """
    Schema for updating user.
    """
    name: str = None
    email: EmailStr = None
    password: str = None


class UserRetrieveListSchema(UserBaseSchema):
    """
    Schema for retrieving list of users or certain user.
    """
    is_active: bool


class UserLoginSchema(BaseModel):
    """
    Schema for login user.
    """
    name: str
    password: str
