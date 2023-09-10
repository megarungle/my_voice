from typing import List, Tuple, Optional

from src.interface import runner
from src.structs import InferStatus, Data

import re
import torch
from transformers import AutoModelForSeq2SeqLM, T5TokenizerFast
import nltk
import string
from nltk.stem.snowball import RussianStemmer
import time

MODEL_NAME = "UrukHan/t5-russian-spell"
MAX_INPUT = 256
PATTERN = "[!@#$%^&*\(\)\-_=+\\\|\[\]\{\}\;\:'\",<.>/?\«\»]+\ *"


class RunnerRecovery(runner.Runner):
    tokenizer: T5TokenizerFast
    model: AutoModelForSeq2SeqLM
    device: torch.device
    neural_preprocess: bool = True

    def __new__(
        cls, neural_preprocess: bool
    ) -> Tuple[InferStatus, Optional[runner.Runner]]:
        print(f"i've got {neural_preprocess} in __new__")
        cls.neural_preprocess = neural_preprocess
        if torch.cuda.is_available():
            cls.device = torch.device("cuda")
        else:
            cls.device = torch.device("cpu")
        # Temporary force CPU due to problem with CUDA
        cls.device = torch.device("cpu")
        print(f"Recovery initialization on {cls.device} device...")
        try:
            cls.tokenizer = T5TokenizerFast.from_pretrained(MODEL_NAME)
            cls.model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
        except Exception as exc:
            print(f"Recovery runner initialization failed: {exc}")
            return InferStatus.status_error_init
        print("Done")
        return (InferStatus.status_ok, super(RunnerRecovery, cls).__new__(cls))

    def _preprocess_nltk(self, data):
        text = data
        # токенизируем текст и удаляем пунктуацию
        tokens = nltk.word_tokenize(text)
        tokens = [word for word in tokens if word.isalnum()]

        # исправляем орфографические ошибки
        corrected_tokens = []
        for token in tokens:
            stem_l = self.stemmer.stem(token)
            corrected_tokens.append(stem_l)
        return " ".join(corrected_tokens)

    def infer(self, data, question) -> Tuple[InferStatus, List[Data]]:
        final_status = InferStatus.status_ok

        # загружаем русский язык для NLTK
        nltk.download("punkt")
        nltk.download("averaged_perceptron_tagger")
        nltk.download("tagsets")
        nltk.download("words")
        nltk.download("maxent_ne_chunker")
        nltk.download("stopwords")
        self.stemmer = RussianStemmer()
        big_input = len(data) > MAX_INPUT
        corrected = []
        for i in range(0, len(data)):
            punctuation_corrected = self._correct_punctuation(data[i].answer)
            corrected.append(punctuation_corrected)

        out = []
        print(f"i've got {self.neural_preprocess} in infer")
        if self.neural_preprocess:
            print("Using urukhan preprocessing")
            final_status, out = self._correct_spelling(corrected)
        else:
            print("Using nltk preprocessing")
            for i in range(0, len(corrected)):
                out.append(self._preprocess_nltk(corrected[i]))

        for i in range(0, len(data)):
            data[i].corrected = self._correct_punctuation(out[i])

        return [final_status, data]

    def _correct_spelling(
        self, input_sequences: List[str]
    ) -> Tuple[InferStatus, Optional[List[str]]]:
        # Prepare input
        try:
            encoded = self.tokenizer(
                ["Spell correct: " + sequence for sequence in input_sequences],
                padding="longest",
                max_length=MAX_INPUT,
                truncation=True,
                return_tensors="pt",
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
        for i in range(len(res)):
            res[i] = res[i].lower()
        return (InferStatus.status_ok, res)

    def _correct_punctuation(self, input_phrase) -> str:
        try:
            if input_phrase:
                input_phrase = re.sub(PATTERN, " ", input_phrase)
                input_phrase = re.sub(" +", " ", input_phrase)
        except Exception as exc:
            print(f"ERROR: recovery runner correction punctuation failed: {exc}")
        return input_phrase
