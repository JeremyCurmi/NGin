from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.core import dependencies as deps
from src import schemas
from src.crud import ModelVersionCrud

router = APIRouter(prefix="/model_version", tags=["model_version"])


@router.get("/")
async def get_model_versions():
    return ["model version 1", "model version 2"]


@router.post("/", response_model=schemas.ModelVersion, status_code=201)
async def create_model_version(
    model_version: schemas.ModelVersionCreate, db: Session = Depends(deps.get_db)
):
    return ModelVersionCrud(db).create(model_version)
