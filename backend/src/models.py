from pydantic import BaseModel, Field


class SpellCorrectRequest(BaseModel):
    input: str = Field(..., example="сеглдыя хорош ден")  # min, max len

    class Config:
        json_schema_extra = {"example": {"input": "сеглдыя хорош ден"}}
