from typing import List, Tuple

from my_voice.backend.src.interface import runner
from my_voice.backend.src.structs import InferStatus, Data

class RunnerSentiment(runner.Runner):
    def __init__(self) -> None:
        print("Sentiment initialization")

    def infer(self, data) -> Tuple[InferStatus, List[Data]]:
        pass