from typing import List, Dict

from pydantic import BaseModel, Field


class SpellCorrectRequest(BaseModel):
    input: str = Field(..., example="сеглдыя хорош ден")


class SentimentRequest(BaseModel):
    input: str = Field(..., example="заниматься хакатоном")


class InferInputAnswer(BaseModel):
    answer: str
    count: int

    class Config:
        json_schema_extra = {
            "example": {"answer": "создание раб.групп для контрол", "count": 1}
        }


class InferRequest(BaseModel):
    sense: int
    neural_preprocess: bool
    question: str
    id: int
    answers: List[InferInputAnswer]

    class Config:
        json_schema_extra = {
            "example": {
                "sense": 80,
                "neural_preprocess": False,
                "question": "Вопрос 7. Что должны сделать Лидеры безопасности, чтобы снизить травматизм?",
                "id": 19749,
                "answers": [{"answer": "создание раб.групп для контрол", "count": 1}],
            }
        }


class InferOutputAnswer(BaseModel):
    answer: str
    count: int
    cluster: str
    sentiment: str
    corrected: str


class InferOutput(BaseModel):
    data: List[InferOutputAnswer]


class SentimentResult(BaseModel):
    label: str
    score: float

    class Config:
        json_schema_extra = {
            "example": {"label": "neutral", "score": "0.9434003233909607"}
        }


class InferInputAnswer(BaseModel):
    theme: str
    answers: List[str]


class Themes(BaseModel):
    positive: List[InferInputAnswer]
    negative: List[InferInputAnswer]
    neutral: List[InferInputAnswer]

    class Config:
        json_schema_extra = {
            "example": {
                "positive": [{"theme": "str", "answers": ["str1", "str2"]}],
                "negative": [{"theme": "str", "answers": ["str1", "str2"]}],
                "neutral": [{"theme": "str", "answers": ["str1", "str2"]}],
            }
        }
