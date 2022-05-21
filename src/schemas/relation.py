from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserModelBase(BaseModel):
    pass


class UserModelCreate(UserModelBase):
    user_id: int
    model_id: int

    def parser(self) -> dict:
        return {
            "user_id": self.user_id,
            "model_id": self.model_id,
        }

class UserModelUpdate(UserModelBase):
    pass


class UserModelInDBBase(UserModelBase):
    pass

    class Config:
        orm_mode = True


class UserModel(UserModelInDBBase):
    """Additional properties to return via API"""
    user_id: int
    model_id: int


class UserModelInDB(UserModelInDBBase):
    """Additional properties saved in db"""

    pass


class ModelModelVersionBase(BaseModel):
    model_id: int


class ModelModelVersionCreate(ModelModelVersionBase):
    model_version_id: int


class ModelModelVersionUpdate(ModelModelVersionBase):
    pass


class ModelModelVersionInDBBase(ModelModelVersionBase):
    pass

    class Config:
        orm_mode = True


class ModelModelVersion(ModelModelVersionInDBBase):
    """Additional properties to return via API"""

    pass


class ModelModelVersionInDB(ModelModelVersionInDBBase):
    """Additional properties saved in db"""

    pass
