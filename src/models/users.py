from datetime import datetime
from src.db import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=False)
    created_at = Column(DateTime, default=datetime.utcnow)
