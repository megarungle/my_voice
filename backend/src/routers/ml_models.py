from fastapi import APIRouter
from typing import List

from src.ml_scripts import spelling
from src.models import SpellCorrectRequest

models_router = APIRouter()


@models_router.get("/")
def get_models():
    return {"hello": "world"}


@models_router.get("/spellcheck")
def post_spellcheck(text: str) -> List[str]:
    return spelling.spell_correct([text])  # FIXME: Use proper model
