from fastapi import FastAPI, Depends
from .core.config import Settings
from .db.session import engine
from .db.models.base import BaseClass
from functools import lru_cache

from .apis.base import router


@lru_cache()
def get_settings():
    return Settings()


def create_tables():
    BaseClass.metadata.create_all(bind=engine)


def start_application():
    settings = get_settings()
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    app.include_router(router)
    create_tables()
    return app


app = start_application()


@app.get("/")
async def home():
    return {"data": "hello world"}
