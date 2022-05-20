from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserBase(BaseModel):
    full_name: str | None
    email: EmailStr | None
    is_active: bool | None = True


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    pass


class UserInDBBase(UserBase):
    id: int
    created_at: datetime
    update_at: datetime
    # TODO: user role


class User(UserInDBBase):
    """Additional properties to return via API"""
    pass


class UserInDB(UserInDBBase):
    """Additional properties saved in db"""
    hashed_password: str