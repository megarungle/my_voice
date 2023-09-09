from typing import List, Tuple

from my_voice.backend.src.interface import runner
from my_voice.backend.src.structs import InferStatus, Data

class RunnerCluster(runner.Runner):
    def __init__(self) -> None:
        print("Cluster initialization")

    def infer(self, data, question) -> Tuple[InferStatus, List[Data]]:
        pass