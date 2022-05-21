from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from src.core import dependencies as deps
from src import schemas
from src.crud import UserModelCrud


router = APIRouter(prefix="/relations", tags=["relations","user_model"])


@router.get("/user_model", response_model=List[schemas.UserModel], status_code=200)
async def get_all(db: Session = Depends(deps.get_db)):
    return UserModelCrud(db).get_all()


@router.post("/user_model", response_model=schemas.UserModel, status_code=201)
async def create_user_model(user_model: schemas.UserModelCreate, db: Session = Depends(deps.get_db)):
    return UserModelCrud(db).create(user_model)


@router.get("/user_model/{user_id}", response_model=List[schemas.UserModel], status_code=200)
async def get_by_user_id(user_id: int, db: Session = Depends(deps.get_db)):
    return UserModelCrud(db).get_by_id(user_id)