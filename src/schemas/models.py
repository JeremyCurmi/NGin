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

    class Config:
        orm_mode = True


class ModelType(ModelTypeInDBBase):
    """Additional properties to return via API"""

    pass


class ModelTypeInDB(ModelTypeInDBBase):
    """Additional properties saved in db"""

    pass


class ModelBase(BaseModel):
    model_id: int = -1


class ModelCreate(ModelBase):
    name: str
    description: str

    def parser(self) -> dict:
        return {
            "name": self.name,
            "model_id": self.model_id,
            "description": self.description,
        }


class ModelUpdate(ModelBase):
    pass


class ModelInDBBase(ModelBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class Model(ModelInDBBase):
    """Additional properties to return via API"""

    pass


class ModelInDB(ModelInDBBase):
    """Additional properties saved in db"""

    pass


class ModelVersionBase(BaseModel):
    model_version_id: int = -1


class ModelVersionCreate(ModelVersionBase):
    description: str

    def parser(self):
        return {"model_version_id": self.model_version_id,
                "description": self.description}



class ModelVersionUpdate(ModelVersionBase):
    pass


class ModelVersionInDBBase(ModelVersionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class ModelVersion(ModelVersionInDBBase):
    """Additional properties to return via API"""

    pass


class ModelVersionInDB(ModelVersionInDBBase):
    """Additional properties saved in db"""

    pass
