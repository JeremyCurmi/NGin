from sqlalchemy.orm import Session
from typing import List, Optional

from .base import DBCrud
from src.models import UserModel
from src.schemas import UserModelCreate, UserModelUpdate


class UserModelCrud(DBCrud):
    def __init__(self, db: Session):
        self.db = db
        self.model = UserModel

    def create(self, model: UserModelCreate) -> UserModel:
        model_ = model.parser()
        return self.save(self.model(**model_))

    def get_by_id(self, id: int) -> Optional[UserModel]:
        return super().get_by_id(id)

    # TODO: remove abstractmethod properties
    # TODO: def get_by_user_id
    # TODO: def get_by_model_id

    def get_all(self, limit: int = 0) -> List[UserModel]:
        return super().get_all(limit)

    def delete_by_id(self, id: int) -> UserModel:
        return super().delete_by_id(id)

    def update(self, id: str | int, model: UserModelUpdate) -> UserModel:
        return super().update(id, model.dict())
