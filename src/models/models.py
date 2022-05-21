from src.db import Base
from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)
from sqlalchemy.orm import relationship


class ModelType(Base):
    __tablename__ = "modelType"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # model = relationship("ModelModelType", back_populates="ModelType")

    def __repr__(self) -> str:
        return f"Type={self.name}"


class Model(Base):
    __tablename__ = "model"

    id = Column(Integer, primary_key=True, autoincrement=True)
    model_id = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False, unique=False)
    description = Column(String(255), nullable=False, unique=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # model_type = relationship("ModelModelType", back_populates="Model")
    # user = relationship("userModel", back_populates="Model")
    # model_version = relationship("ModelModelVersion", back_populates="Model")

    def __repr__(self):
        return f"Model {self.id}, model_id {self.model_id}"


class ModelVersion(Base):
    __tablename__ = "modelVersion"
    id = Column(Integer, primary_key=True, autoincrement=True)
    model_version_id = Column(Integer, nullable=False)
    description = Column(String(255), nullable=False, unique=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # model = relationship("ModelModelVersion", back_populates="ModelVersion")

    def __repr__(self):
        return f"Model Version {self.id}, model_version_id {self.model_version_id}"
