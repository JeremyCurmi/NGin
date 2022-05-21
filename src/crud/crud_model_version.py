from sqlalchemy.orm import Session
from typing import List, Optional

from .base import DBCrud
from src.models import ModelVersion
from src.schemas import ModelVersionCreate, ModelVersionUpdate


class ModelVersionCrud(DBCrud):
    def __init__(self, db: Session):
        self.db = db
        self.model = ModelVersion

    def create(self, model: ModelVersionCreate) -> ModelVersion:
        model_ = model.parser()
        return self.save(self.model(**model_))

    def get_by_id(self, id: int) -> Optional[ModelVersion]:
        return super().get_by_id(id)

    def get_all(self, limit: int = 0) -> List[ModelVersion]:
        return super().get_all(limit)

    def delete_by_id(self, id: int) -> ModelVersion:
        return super().delete_by_id(id)

    def update(self, id: str | int, model: ModelVersionUpdate) -> ModelVersion:
        return super().update(id, model.dict())
