from pydantic import BaseModel, EmailStr


class UserBaseSchema(BaseModel):
    name: str
    email: EmailStr


class UserCreateUpdateSchema(UserBaseSchema):
    password: str


class UserRetrieveListSchema(UserBaseSchema):
    is_active: bool


class UserUpdateSchemaForAdmin(UserBaseSchema):
    hashed_password: str
    is_superuser: bool


class UserRetrieveListSchemaForAdmin(UserBaseSchema):
    id: int
    hashed_password: str
    is_superuser: bool
    is_active: bool
