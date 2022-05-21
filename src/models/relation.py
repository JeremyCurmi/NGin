from src.db import Base
from sqlalchemy import (
    Column,
    Integer,
    ForeignKey
)
from sqlalchemy.orm import relationship


class UserModel(Base):
    __tablename__ = "userModel"

    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True, nullable=False)
    model_id = Column(Integer, ForeignKey("model.id"), primary_key=True, nullable=False)

    users = relationship("User", backref="model")
    models = relationship("Model", backref="user")


class ModelModelType(Base):
    __tablename__ = "modelModelType"

    model_id = Column(Integer, ForeignKey("model.id"), primary_key=True, nullable=False)
    model_type_id = Column(Integer, ForeignKey("model_type.id"), primary_key=True, nullable=False)

    model = relationship("Model", backref="model_type")


class ModelModelVersion(Base):
    __tablename__ = "modelModelVersion"

    model_id = Column(Integer, ForeignKey("model.id"), primary_key=True, nullable=False)
    model_version_id = Column(Integer, ForeignKey("modelVersion.id"), primary_key=True, nullable=False)

    model=relationship("Model", backref="version")
    version=relationship("ModelVersion", backref="model")