from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from src.core import dependencies as deps
from src import schemas
from src.crud import ModelCrud

router = APIRouter(prefix="/model", tags=["model"])


@router.get("/", response_model=List[schemas.Model], status_code=200)
async def get_models(db: Session = Depends(deps.get_db)):
    return ModelCrud(db).get_all()


@router.post("/", response_model=schemas.Model, status_code=201)
async def create_model(model: schemas.ModelCreate, db: Session = Depends(deps.get_db)):
    # TODO: get current user (from dependency)
    user_id = 1

    # TODO: get count distinct row for user in userModel Table
    # TODO: model_id = 👆 + 1
    # TODO: create new row in Model (model_id)
    # TODO: create new row in userModel (user_id, model_id)
    # TODO: create new row in modelModelType

    # TODO: create_new_model_version method in model_version.py (different from create model version)
    # TODO: create new row in modelVersion with model_version_id = 1
    # TODO: create new row in modelModelVersion

    return ModelCrud(db).create(model)
