from datetime import datetime
from src.db import Base
from sqlalchemy import (
    Column,
    Boolean,
    Integer,
    String,
    DateTime,
)
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String(50), nullable=False, unique=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    update_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    model_id = relationship("UserModel", back_populates="user")

    def __repr__(self) -> str:
        return f"user {self.id}, full_name={self.full_name}, email={self.email}"

