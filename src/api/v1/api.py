from fastapi import APIRouter
from src.api.v1.routers import api_user, api_model, api_model_version, api_relation

api_router = APIRouter()
api_router.include_router(api_user.router)
api_router.include_router(api_model.router)
api_router.include_router(api_model_version.router)
api_router.include_router(api_relation.router)