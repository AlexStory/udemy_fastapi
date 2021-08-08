from fastapi import FastAPI
from .core.config import settings
from .db.session import engine
from .db.base_class import BaseClass


def create_tables():
    BaseClass.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()
    return app


app = start_application()


@app.get("/")
def home():
    return {"data": "hello world"}
