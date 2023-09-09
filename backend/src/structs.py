from dataclasses import dataclass
from enum import Enum

class Sentiment(Enum):
    negative = -1
    neutral = 0
    positive = 1

class InferStatus(Enum):
    status_ok = 0
    status_error = -1

@dataclass
class Data:
    answer: str = ''
    count: int = 0
    cluster: str = ''
    sentiment: Sentiment = None
    corrected: str = ''
    
    @classmethod
    def fromJson(cls, dict):
        return cls(
            dict["user_id"], dict["login"],
            dict["first_name"], dict["second_name"], dict["middle_name"],
            dict["algs_id"], dict["bound_ids"]
        )
