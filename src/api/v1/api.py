from fastapi import APIRouter
from src.api.v1.routers import user, model, model_version

api_router = APIRouter()
api_router.include_router(user.router)
api_router.include_router(model.router)
api_router.include_router(model_version.router)
