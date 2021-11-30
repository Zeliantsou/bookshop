from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.api import api_router
from core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f'{settings.API_V1_STR}/openapi.json',
)
app = FastAPI()


if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)
