from typing import List, Tuple

from my_voice.backend.src.interface import runner
from my_voice.backend.src.structs import InferStatus, Data

class RunnerRecovery(runner.Runner):
    def __init__(self) -> None:
        print("Recovery initialization")
    
    def infer(self, data) -> Tuple[InferStatus, List[Data]]:
        pass
