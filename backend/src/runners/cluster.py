from typing import List, Tuple

from backend.src.interface import runner
from backend.src.structs import InferStatus, Data


class RunnerCluster(runner.Runner):
    def __init__(self) -> None:
        print("Cluster initialization")

    def infer(self, data, question) -> Tuple[InferStatus, List[Data]]:
        pass