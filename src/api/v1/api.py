from fastapi import APIRouter
from src.api.v1.routers import ml_model

api_router = APIRouter()
api_router.include_router(ml_model.router)
