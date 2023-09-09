from pathlib import Path
from typing import Any, Dict, List


from fastapi import APIRouter

# from backend.src.ml_scripts import spelling, sentiment
from src.models import SentimentResult, SpellCorrectRequest, SentimentRequest, Themes, Answer
from src.utils import parse_dataset_json


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
def get_test() -> Themes:
    test_data =  Path(__file__).parent.resolve().parents[1] / "dataset/labeled/25728.json"
    sents = parse_dataset_json(test_data)

    return Themes(positive = [Answer(theme=theme, answers=[ans for ans in sents["positives"][theme]["answers"]]) for theme in sents["positives"].keys()],
           negative = [Answer(theme=theme, answers=[ans for ans in sents["negatives"][theme]["answers"]]) for theme in sents["negatives"].keys()],
           neutral = [Answer(theme=theme, answers=[ans for ans in sents["neutrals"][theme]["answers"]]) for theme in sents["neutrals"].keys()]
           )
        