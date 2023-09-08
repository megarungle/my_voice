from fastapi import APIRouter

from src.ml_scripts import spelling, sentiment
from src.models import SentimentResult, SpellCorrectRequest, SentimentRequest

models_router = APIRouter()


@models_router.post("/spellcheck")
def post_spellcheck(text: SpellCorrectRequest) -> str:
    return spelling.correct_spelling(text.input)  # FIXME: Use proper model

@models_router.post("/sentiment")
def post_sentiment(text: SentimentRequest) -> SentimentResult:
    res = sentiment.get_sentiment(text.input)
    return SentimentResult(label=res.label, score=res.score)
