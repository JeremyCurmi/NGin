from sqlalchemy.orm import Session
from pydantic import UUID4
from typing import Union, Optional

from .base import DBCrud
from src import models, schemas


class UserCrud(DBCrud):
    def __init__(self, db: Session):
        self.db = db
        self.model = models.User

    def create(self, user: schemas.UserCreate) -> models.User:
        return self.save()

    def get_by_id(self, id: Union[str, UUID4]) -> Optional[models.User]:
        return super().get_by_id(id)