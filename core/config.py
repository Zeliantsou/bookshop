import os
from typing import Any, Union, List, Dict, Optional

from pydantic import BaseSettings, AnyHttpUrl, EmailStr, PostgresDsn, validator


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    SECRET_KEY: str = os.environ.get('SECRET_KEY')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES')
    REFRESH_TOKEN_EXPIRE_MINUTES: int = os.environ.get('REFRESH_TOKEN_EXPIRE_MINUTES')
    SERVER_NAME: str = os.environ.get('SERVER_NAME')
    SERVER_HOST: AnyHttpUrl = os.environ.get('SERVER_HOST')
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = os.environ.get('BACKEND_CORS_ORIGINS')

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str = 'BookShop'

    POSTGRES_SERVER: str = os.environ.get('POSTGRES_SERVER')
    POSTGRES_USER: str = os.environ.get('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.environ.get('POSTGRES_PASSWORD')
    POSTGRES_DB: str = os.environ.get('POSTGRES_DB')
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    FIRST_SUPERUSER: str = os.environ.get('FIRST_SUPERUSER')
    FIRST_SUPERUSER_EMAIL: EmailStr = os.environ.get('FIRST_SUPERUSER_EMAIL')
    FIRST_SUPERUSER_PASSWORD: str = os.environ.get('FIRST_SUPERUSER_PASSWORD')
    USERS_OPEN_REGISTRATION: bool = False

    class Config:
        case_sensitive = True


settings = Settings()

# {
#   "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MzgyNzkxNjgsInN1YiI6IjEifQ.MWlg0KrPSEr1C-_k1KtmEQ4ykDcctOptc8_d6FXuj-M",
#   "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MzgzNjU1NjgsInN1YiI6IjEifQ.pFA69Mu5xMGtj3GuwX9Yj07e_5NiYp5MBsJn22P0Hrg"
# }

# {
#   "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MzgyODcxODcsInN1YiI6IjQifQ.-QjOMK2k35LKfb6rlIhWw5pcOSv0t9NPbVRlcE8bR2s",
#   "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MzgzNzM1ODcsInN1YiI6IjQifQ.7yCGPzqze2zP3SUh5hyBleqLdHUxTJNMYtKkcePHcNU"
# }