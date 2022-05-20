from fastapi import APIRouter

router = APIRouter(prefix="/model", tags=["model"])


@router.get("/")
async def get_models():
    return ["model 1", "model 2"]


@router.post("/")
async def create_model():
    # TODO: get current user (from dependency)
    # TODO: get count distinct row for user in userModel Table
    # TODO: model_id = 👆 + 1
    # TODO: create new row in Model (model_id)
    # TODO: create new row in userModel (user_id, model_id)
    # TODO: create new row in modelModelType

    # TODO: create_new_model_version method in model_version.py (different from create model version)
    # TODO: create new row in modelVersion with model_version_id = 1
    # TODO: create new row in modelModelVersion
    return "model created"
