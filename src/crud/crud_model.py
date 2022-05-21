from sqlalchemy.orm import Session
from typing import List, Optional

from .base import DBCrud
from src.models import Model
from src.schemas import ModelCreate, ModelUpdate


class ModelCrud(DBCrud):
    def __init__(self, db: Session):
        self.db = db
        self.model = Model

    def create(self, model: ModelCreate) -> Model:
        model_ = model.parser()
        return self.save(self.model(**model_))

    def get_by_id(self, id: int) -> Optional[Model]:
        return super().get_by_id(id)

    def get_all(self, limit: int = 0) -> List[Model]:
        return super().get_all(limit)

    def delete_by_id(self, id: int) -> Model:
        return super().delete_by_id(id)

    def update(self, id: str | int, model: ModelUpdate) -> Model:
        return super().update(id, model.dict())
