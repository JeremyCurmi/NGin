from fastapi import APIRouter

router = APIRouter(prefix="/model", tags=["model"])


@router.get("/")
async def get_test():
    return {"ml model endpoint test"}
