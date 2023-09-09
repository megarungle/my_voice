from typing import List, Tuple
from my_voice.backend.src.structs import Data, InferStatus

import abc

class Runner(abc.ABC):
    @abc.abstractmethod
    def infer(self, data, question) -> Tuple[InferStatus, List[Data]]:
        pass
