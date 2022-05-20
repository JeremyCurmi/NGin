from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.core import dependencies as deps


router = APIRouter(prefix="/user", tags=["users"])


@router.get("/")
async def get_users(db:Session = Depends(deps.get_db)):
    return ["user 1", "user 2"]


@router.post("/")
async def create_user(db: Session = Depends(deps.get_db)):
    return "user created"
