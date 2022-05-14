from src.db import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
)


class ModelType(Base):
    __tablename__ = "modelType"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)

    def __repr__(self) -> str:
        return f"Type={self.name}"
