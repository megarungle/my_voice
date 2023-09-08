from typing import List

from pydantic import BaseModel


class SpellCorrectRequest(BaseModel):
    input: str
