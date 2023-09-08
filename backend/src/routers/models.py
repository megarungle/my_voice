from fastapi import APIRouter

models_router = APIRouter()


@models_router.get("/")
def get_models():
    return {"hello": "world"}
