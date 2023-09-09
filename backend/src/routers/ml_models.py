from fastapi import APIRouter

# from backend.src.ml_scripts import spelling, sentiment
# from backend.src.models import SentimentResult, SpellCorrectRequest, SentimentRequest
from pathlib import Path
import json
from typing import Any, Dict, List

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

from collections import namedtuple

@models_router.get("/test")
def get_test() -> Any:
    # TODO: This is a mess. Refactor this
    test_data =  Path(__file__).parent.resolve().parents[1] / "dataset/labeled/25728.json"

    with open(test_data, 'r', encoding='utf-8-sig') as file:
        data = json.load(file)

    parsed_results = {
        "positives": {},
        "negatives": {},
        "neutrals": {}
    }
    Answer = namedtuple("Answer", ["answer", "sentiment"])
    themes: Dict[str, List[Answer]]= {}
    for item in data["answers"]:
        if item["cluster"] in themes:
            themes[item["cluster"]] += [Answer(item["answer"], item["sentiment"])] 
        else:
            themes[item["cluster"]] = [Answer(item["answer"], item["sentiment"])] 

    for theme, answers in themes.items():
        for answer in answers:
            if theme in parsed_results[answer.sentiment].keys():
                parsed_results[answer.sentiment][theme]["answers"].append(answer.answer)
            else:
                parsed_results[answer.sentiment][theme] = {"answers": [answer.answer]}

    return parsed_results
        