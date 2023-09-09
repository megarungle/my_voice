from dataclasses import dataclass
from enum import Enum


class Sentiment(Enum):
    negative = -1
    neutral = 0
    positive = 1


class InferStatus(Enum):
    status_ok = 0
    status_error_init = -1
    status_error_prepare = -2
    status_error_infer = -3


@dataclass
class Data:
    answer: str = ''
    count: int = 0
    cluster: str = ''
    sentiment: Sentiment = None
    corrected: str = ''

    @classmethod
    def fromJson(cls, answer):
        return cls(answer['answer'], answer['count'])

    def data_print(self):
        print("Answer: ", self.answer)
        print("Count: ", self.count)
        print("Cluster: ", self.cluster)
        print("Sentiment: ", self.sentiment)
        print("Corrected: ", self.corrected)
        print("============================")