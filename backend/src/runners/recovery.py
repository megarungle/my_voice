from typing import List, Tuple, Optional

from my_voice.backend.src.interface import runner
from my_voice.backend.src.structs import InferStatus, Data

import torch
from transformers import AutoModelForSeq2SeqLM, T5TokenizerFast

MODEL_NAME = "UrukHan/t5-russian-spell"
MAX_INPUT = 256

class RunnerRecovery(runner.Runner):
    tokenizer: T5TokenizerFast
    model: AutoModelForSeq2SeqLM
    device: torch.device

    def __new__(cls) -> Tuple[InferStatus, Optional[runner.Runner]]:
        if torch.cuda.is_available():
            cls.device = torch.device("cuda")
        else:
            cls.device = torch.device("cpu")
        # Temporary force CPU due to problem with CUDA
        cls.device = torch.device("cpu")
        print(f"Recovery initialization on {cls.device} device")
        try:
            cls.tokenizer = T5TokenizerFast.from_pretrained(MODEL_NAME)
            cls.model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
        except Exception as exc:
            print(f"Recovery runner initialization failed: {exc}")
            return InferStatus.status_error_init
        return (InferStatus.status_ok, super(RunnerRecovery, cls).__new__(cls))

    def infer(self, data, question) -> Tuple[InferStatus, List[Data]]:
        final_status = InferStatus.status_ok
        for i in range(0, len(data)):
            status, out = self._correct_spelling(data[i].answer)
            if status is not InferStatus.status_ok:
                # Не добавляем ничего в результат, но продолжаем обработку
                final_status = status
                continue
            # TODO: add postprocessing with deleting pmarks
            data[i].corrected = out
        return [final_status, data]

    def _correct_spelling(self, input_phrase: str) -> Tuple[InferStatus, Optional[str]]:
        # Prepare input
        try:
            encoded = self.tokenizer(
                [f"Spell correct: {input_phrase}"],
                padding = "longest",
                max_length = MAX_INPUT,
                truncation = True,
                return_tensors = "pt",
            )
        except Exception as exc:
            print(f"ERROR: recovery runner input preparing failed: {exc}")
            return InferStatus.status_error_prepare
        # Infer
        try:
            predicts = self.model.generate(**encoded.to(self.device))
            res = self.tokenizer.batch_decode(predicts, skip_special_tokens=True)
        except Exception as exc:
            print(f"ERROR: recovery runner infer failed: {exc}")
            return InferStatus.status_error_infer
        # Output
        return (InferStatus.status_ok, res[0].lower())
