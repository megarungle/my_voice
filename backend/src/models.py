from typing import List

from pydantic import BaseModel, Field


class SpellCorrectRequest(BaseModel):
    input: str = Field(..., example="сеглдыя хорош ден")


class SentimentRequest(BaseModel):
    input: str = Field(..., example="заниматься хакатоном")

class SentimentResult(BaseModel):
    label: str
    score: float

    class Config:
        json_schema_extra = {"example": {"label": "neutral", "score": "0.9434003233909607"}}