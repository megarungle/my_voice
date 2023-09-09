from pathlib import Path
from typing import Any, Dict, List
from collections import defaultdict

from fastapi import APIRouter

from src.ml_scripts import spelling, sentiment
from src.models import (
    SentimentResult,
    SpellCorrectRequest,
    SentimentRequest,
    InferRequest,
    InferOutputAnswer,
    InferInputAnswer,
    Themes,
    InferOutput,
)
from src.utils.dataset_parser import parse_dataset_json
from src.core import Core
from src.structs import InferStatus, Data

from typing import List


models_router = APIRouter()


@models_router.post("/spellcheck")
def post_spellcheck(text: SpellCorrectRequest) -> str:
    return spelling.correct_spelling(text.input)  # FIXME: Use proper model


@models_router.post("/sentiment")
def post_sentiment(text: SentimentRequest) -> SentimentResult:
    res = sentiment.get_sentiment(text.input)
    return SentimentResult(label=res.label, score=res.score)


@models_router.post("/infer")
def post_infer(_input: InferRequest) -> Any:  # TODO: Use model instead of Any
    answers = []

    _input = _input.model_dump()

    class Infer:
        def get_redirect_url(self, _input):
            core = Core()
            print("Waiting for infer request")
            status, data = core.infer(_input)
            if status is InferStatus.status_ok:
                for answer in data:
                    # answer.data_print()
                    answers.append(answer)
            return "new_url"

    infer = Infer()
    infer.get_redirect_url(_input)
    return answers


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
            InferInputAnswer(
                theme=theme,
                answers=answers,
            )
            for theme, answers in answers["positives"].items()
        ],
        negative=[
            InferInputAnswer(
                theme=theme,
                answers=answers,
            )
            for theme, answers in answers["negatives"].items()
        ],
        neutral=[
            InferInputAnswer(theme=theme, answers=answers)
            for theme, answers in answers["neutrals"].items()
        ],
    )
