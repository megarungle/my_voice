from fastapi import APIRouter

# from backend.src.ml_scripts import spelling, sentiment
# from backend.src.models import SentimentResult, SpellCorrectRequest, SentimentRequest
from pathlib import Path
import json
from typing import Any

models_router = APIRouter()


# @models_router.post("/spellcheck")
# def post_spellcheck(text: SpellCorrectRequest) -> str:
#     return spelling.correct_spelling(text.input)  # FIXME: Use proper model
#
#
# @models_router.post("/sentiment")
# def post_sentiment(text: SentimentRequest) -> SentimentResult:
#     res = sentiment.get_sentiment(text.input)
#     return SentimentResult(label=res.label, score=res.score)


@models_router.get("/test")
def get_test() -> Any:
    script_dir = Path(__file__).parent.resolve().parents[1]
    mypath = script_dir / 'dataset/labeled/25728.json'

    with open(mypath, 'r', encoding='utf-8-sig') as file:
        print(file)
        data = json.load(file)

    return data
