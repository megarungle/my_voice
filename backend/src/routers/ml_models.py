from typing import List
from pathlib import Path
from collections import defaultdict

from fastapi import APIRouter

from src.ml_scripts import spelling, sentiment
from src.models import (
    SentimentResult,
    SpellCorrectRequest,
    SentimentRequest,
    InferRequest,
    InferInputAnswer,
    Themes,
)
from src.utils.dataset_parser import parse_dataset_json
from src.core import Core
from src.structs import InferStatus, Data


models_router = APIRouter()


@models_router.post("/spellcheck")
def post_spellcheck(text: SpellCorrectRequest) -> str:
    return spelling.correct_spelling(text.input)  # FIXME: Use proper model


@models_router.post("/sentiment")
def post_sentiment(text: SentimentRequest) -> SentimentResult:
    res = sentiment.get_sentiment(text.input)
    return SentimentResult(label=res.label, score=res.score)


@models_router.post("/infer")
def post_infer(_input: InferRequest) -> Themes:
    infer_res: List[Data] = []

    _input = _input.model_dump()

    class Infer:
        def get_redirect_url(self, _input):
            core = Core(sense=_input["sense"], preprocess=_input["neural_preprocess"])
            print("Waiting for infer request")

            # Since infer is untested with these params.
            # Removing them just in case
            _input.pop("sense", None)
            _input.pop("neural_preprocess", None)

            status, data = core.infer(_input)
            if status is InferStatus.status_ok:
                for answer in data:
                    # answer.data_print()
                    infer_res.append(answer)
            return "new_url"

    infer = Infer()
    infer.get_redirect_url(_input)

    answers = {
        "positive": defaultdict(list),
        "negative": defaultdict(list),
        "neutral": defaultdict(list),
    }
    for data in infer_res:
        answers[data.sentiment][data.cluster].append(data.answer)

    return Themes(
        positive=[
            InferInputAnswer(
                theme=theme,
                answers=answers,
            )
            for theme, answers in answers["positive"].items()
        ],
        negative=[
            InferInputAnswer(
                theme=theme,
                answers=answers,
            )
            for theme, answers in answers["negative"].items()
        ],
        neutral=[
            InferInputAnswer(theme=theme, answers=answers)
            for theme, answers in answers["neutral"].items()
        ],
    )


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
    for _sentiment, data in sents.items():
        for answer in data:
            answers[_sentiment][answer.theme].append(answer.answer)

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
