from pydantic import BaseModel, EmailStr
from datetime import datetime
from src import core

class UserBase(BaseModel):
    is_active: bool | None = True


class UserCreate(UserBase):
    full_name: str
    email: EmailStr
    password: str

    def parser(self) -> dict:
        return {
            "full_name": self.full_name,
            "email": self.email,
            "hashed_password": core.AuthManager.hash_password(self.password),
        }


class UserUpdate(UserBase):
    pass


class UserInDBBase(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
    # TODO: user role

    class Config:
        orm_mode = True


class User(UserInDBBase):
    """Additional properties to return via API"""

    pass


class UserInDB(UserInDBBase):
    """Additional properties saved in db"""
    pass
    # hashed_password: str
