from src.db import Base
from sqlalchemy import (
    Column,
    Integer,
)
from sqlalchemy.orm import relationship


class UserModel(Base):
    __tablename__ = "userModel"

    user_id = Column(Integer)
    model_id = Column(Integer)

    user = relationship("User", back_populates="userModel")
    model = relationship("Model", back_populates="userModel")


class ModelModelType(Base):
    __tablename__ = "modelModelType"

    model_id = Column(Integer)
    model_type_id = Column(Integer)

    model_type = relationship("ModelType", back_populates="ModelModelType")
    model = relationship("Model", back_populates="ModelModelType")


class ModelModelVersion(Base):
    __tablename__ = "modelModelVersion"

    model_id = Column(Integer)
    model_version_id = Column(Integer)

    model = relationship("Model", back_populates="ModelModelVersion")
    model_version = relationship("ModelVersion", back_populates="ModelModelVersion")