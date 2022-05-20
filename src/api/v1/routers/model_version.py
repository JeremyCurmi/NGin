from fastapi import APIRouter

router = APIRouter(prefix="/model_version", tags=["model_version"])


@router.get("/")
async def get_model_versions():
    return ["model version 1", "model version 2"]


@router.post("/")
async def create_model_version():
    return "model version created"
