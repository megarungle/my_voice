from fastapi import APIRouter

from src.ml_scripts import spelling
from src.models import SpellCorrectRequest

models_router = APIRouter()


@models_router.get("/")
def get_models():
    return {"hello": "world"}


@models_router.post("/spellcheck")
def post_spellcheck(text: SpellCorrectRequest) -> str:
    return spelling.spell_corect(text.input)
