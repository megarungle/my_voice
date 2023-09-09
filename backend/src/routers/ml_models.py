from pathlib import Path
from typing import Any, Dict, List


from fastapi import APIRouter

# from backend.src.ml_scripts import spelling, sentiment
from src.models import (
    SentimentResult,
    SpellCorrectRequest,
    SentimentRequest,
    Themes,
    Answer,
)
from src.utils import parse_dataset_json


models_router = APIRouter()


@models_router.post("/spellcheck")
def post_spellcheck(text: SpellCorrectRequest) -> str:
    return spelling.correct_spelling(text.input)  # FIXME: Use proper model


@models_router.post("/sentiment")
def post_sentiment(text: SentimentRequest) -> SentimentResult:
    res = sentiment.get_sentiment(text.input)
    return SentimentResult(label=res.label, score=res.score)

from collections import defaultdict


@models_router.get("/test")
def get_test() -> Themes:
    test_data = (
        Path(__file__).parent.resolve().parents[1] / "dataset/labeled/25728.json"
    )
    sents = parse_dataset_json(test_data)

    answers = {
        "positives": defaultdict(list),
        "negatives": defaultdict(list),
        "neutrals": defaultdict(list),
    }
    for sentiment, data in sents.items():
        for answer in data:
            answers[sentiment][answer.theme].append(answer.answer)

    return Themes(
        positive=[
            Answer(
                theme=theme,
                answers=answers,
            )
            for theme, answers in answers["positives"].items()
        ],
        negative=[
            Answer(
                theme=theme,
                answers=answers,
            )
            for theme, answers in answers["negatives"].items()
        ],
        neutral=[
            Answer(theme=theme, answers=answers)
            for theme, answers in answers["neutrals"].items()
        ],
    )
