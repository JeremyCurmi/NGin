from pydantic import BaseModel, EmailStr
from datetime import datetime


class ModelTypeBase(BaseModel):
    name: str


class ModelTypeCreate(ModelTypeBase):
    pass


class ModelTypeUpdate(ModelTypeBase):
    pass


class ModelTypeInDBBase(ModelTypeBase):
    id: int
    created_at: datetime


class ModelType(ModelTypeInDBBase):
    """Additional properties to return via API"""
    pass


class ModelTypeInDB(ModelTypeInDBBase):
    """Additional properties saved in db"""
    pass
    

class ModelBase(BaseModel):
    name: str
    description: str



class ModelCreate(ModelBase):
    model_id: int


class ModelUpdate(ModelBase):
    pass


class ModelInDBBase(ModelBase):
    id: int
    created_at: datetime


class Model(ModelInDBBase):
    """Additional properties to return via API"""
    pass


class ModelInDB(ModelInDBBase):
    """Additional properties saved in db"""
    pass


class ModelVersionBase(BaseModel):
    description: str


class ModelVersionCreate(ModelVersionBase):
    model_version_id: int


class ModelVersionUpdate(ModelVersionBase):
    pass


class ModelVersionInDBBase(ModelVersionBase):
    id: int
    created_at: datetime


class ModelVersion(ModelVersionInDBBase):
    """Additional properties to return via API"""
    pass


class ModelVersionInDB(ModelVersionInDBBase):
    """Additional properties saved in db"""
    pass