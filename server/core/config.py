import os
from typing import Set
from dotenv import load_dotenv
from pathlib import Path
from pydantic import BaseSettings

load_dotenv(dotenv_path=".env")


class Settings(BaseSettings):
    PROJECT_TITLE: str = "Job Board"
    PROJECT_VERSION: str = "0.1.0"
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: str = "5432"
    POSTGRES_DB: str
