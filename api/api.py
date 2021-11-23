from fastapi import APIRouter

from api import (
    user_endpoints,
    authors_endpoints,
    books_endpoints,
    login_endpoints,
)


api_router = APIRouter()
api_router.include_router(login_endpoints.router, prefix='/auth', tags=['login'])
api_router.include_router(user_endpoints.router, prefix='/users', tags=['users'])
api_router.include_router(authors_endpoints.router, prefix='/authors', tags=['authors'])
# api_router.include_router(books_endpoints.router, prefix='/books', tags=['books'])
# api_router.include_router(utils_endpoints.router, prefix='/utils', tags=['utils'])
