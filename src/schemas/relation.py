from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserModelBase(BaseModel):
    user_id: int


class UserModelCreate(UserModelBase):
    model_id: int


class UserModelUpdate(UserModelBase):
    pass


class UserModelInDBBase(UserModelBase):
    pass


class UserModel(UserModelInDBBase):
    """Additional properties to return via API"""
    pass


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


class ModelModelVersion(ModelModelVersionInDBBase):
    """Additional properties to return via API"""
    pass


class ModelModelVersionInDB(ModelModelVersionInDBBase):
    """Additional properties saved in db"""
    pass