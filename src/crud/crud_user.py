from sqlalchemy.orm import Session
from typing import List, Optional

from .base import DBCrud
from src.models import User
from src.schemas import UserCreate, UserUpdate


class UserCrud(DBCrud):
    def __init__(self, db: Session):
        self.db = db
        self.model = User

    def create(self, user: UserCreate) -> User:
        model_ = user.parser()
        return self.save(self.model(**model_))

    def get_by_id(self, id: int) -> Optional[User]:
        return super().get_by_id(id)

    def get_all(self, limit: int = 0) -> List[User]:
        return super().get_all(limit)

    def delete_by_id(self, id: int) -> User:
        return super().delete_by_id(id)

    def update(self, id: str | int, user: UserUpdate) -> User:
        return super().update(id, user.dict())
