import os
from typing import Any, Union, List, Dict, Optional

from pydantic import BaseSettings, AnyHttpUrl, EmailStr, PostgresDsn, validator


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    SECRET_KEY: str = os.environ.get('SECRET_KEY', None)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES', None)
    SERVER_NAME: str = os.environ.get('SERVER_NAME', None)
    SERVER_HOST: AnyHttpUrl = os.environ.get('SERVER_HOST', None)
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = os.environ.get('BACKEND_CORS_ORIGINS', None)

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str = 'BookShop'

    POSTGRES_SERVER: str = os.environ.get('POSTGRES_SERVER', None)
    POSTGRES_USER: str = os.environ.get('POSTGRES_USER', None)
    POSTGRES_PASSWORD: str = os.environ.get('POSTGRES_PASSWORD', None)
    POSTGRES_DB: str = os.environ.get('POSTGRES_DB', None)
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = os.environ.get('SQLALCHEMY_DATABASE_URI', None)

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

    FIRST_SUPERUSER: str = os.environ.get('FIRST_SUPERUSER', None)
    FIRST_SUPERUSER_EMAIL: EmailStr = os.environ.get('FIRST_SUPERUSER_EMAIL', None)
    FIRST_SUPERUSER_PASSWORD: str = os.environ.get('FIRST_SUPERUSER_PASSWORD', None)
    USERS_OPEN_REGISTRATION: bool = False

    class Config:
        case_sensitive = True


settings = Settings()
