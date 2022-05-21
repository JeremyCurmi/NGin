from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from src.core import dependencies as deps
from src import schemas
from src.crud import UserCrud


router = APIRouter(prefix="/user", tags=["users"])


@router.get("/", response_model=List[schemas.User], status_code=200)
async def get_users(db: Session = Depends(deps.get_db)):
    return UserCrud(db).get_all()


@router.post("/", response_model=schemas.User, status_code=201)
async def create_user(user: schemas.UserCreate, db: Session = Depends(deps.get_db)):
    return UserCrud(db).create(user)
