from typing import List, Dict

from pydantic import BaseModel, Field


class SpellCorrectRequest(BaseModel):
    input: str = Field(..., example="сеглдыя хорош ден")


class SentimentRequest(BaseModel):
    input: str = Field(..., example="заниматься хакатоном")


class SentimentResult(BaseModel):
    label: str
    score: float

    class Config:
        json_schema_extra = {
            "example": {"label": "neutral", "score": "0.9434003233909607"}
        }


class Answer(BaseModel):
    theme: str
    answers: List[str]


class Themes(BaseModel):
    positive: List[Answer]
    negative: List[Answer]
    neutral: List[Answer]

    class Config:
        json_schema_extra = {
            "example": {
                "positive": [{"theme": "str", "answers": ["str1", "str2"]}],
                "negative": [{"theme": "str", "answers": ["str1", "str2"]}],
                "neutral": [{"theme": "str", "answers": ["str1", "str2"]}],
            }
        }
