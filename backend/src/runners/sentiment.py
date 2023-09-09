from typing import List, Tuple, Optional

from backend.src.interface import runner
from backend.src.structs import InferStatus, Data

from transformers import pipeline
import torch

MODEL_NAME = "seara/rubert-tiny2-russian-sentiment"

class RunnerSentiment(runner.Runner):
    model: None
    device: torch.device

    def __new__(cls) -> Tuple[InferStatus, Optional[runner.Runner]]:
        if torch.cuda.is_available():
            cls.device = torch.device("cuda")
        else:
            cls.device = torch.device("cpu")
        # Temporary force CPU due to problem with CUDA
        cls.device = torch.device("cpu")
        print(f"Sentiment initialization on {cls.device} device...")
        try:
            cls.model = pipeline(model=MODEL_NAME)
        except Exception as exc:
            print(f"Sentiment runner initialization failed: {exc}")
            return InferStatus.status_error_init
        print("Done")
        return (InferStatus.status_ok, super(RunnerSentiment, cls).__new__(cls))


    def infer(self, data) -> Tuple[InferStatus, List[Data]]:
        final_status = InferStatus.status_ok
        for i in range(0, len(data)):
            status, out = self._get_sentiment(data[i].answer)
            if status is not InferStatus.status_ok:
                # Не добавляем ничего в результат, но продолжаем обработку
                final_status = status
                continue
            data[i].sentiment = out
        return [final_status, data]

    def _get_sentiment(self, input_phrase: str) -> Tuple[InferStatus, Optional[str]]:
        # Infer
        try:
            res = self.model(input_phrase)
        except Exception as exc:
            print(f"ERROR: sentiment runner infer failed: {exc}")
            return InferStatus.status_error_infer
        # Output
        return (InferStatus.status_ok, res[0]['label'])
