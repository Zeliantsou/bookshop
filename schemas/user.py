from pydantic import BaseModel, EmailStr


class UserBaseSchema(BaseModel):
    name: str
    email: EmailStr

    class Config:
        orm_mode = True


class UserCreateSchema(UserBaseSchema):
    password: str


class CreateFirstSuperuserSchema(UserCreateSchema):
    is_superuser: bool


class UserUpdateSchema(UserBaseSchema):
    name: str = None
    email: EmailStr = None
    password: str = None


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


class UserLoginSchema(BaseModel):
    name: str
    password: str
