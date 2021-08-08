from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class BaseClass:
    id: Any
    __name__: str

    def __table_name__(cls) -> str:
        return cls.__name__.lower()
