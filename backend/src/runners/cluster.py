from typing import List, Tuple, Optional

from src.interface import runner
from src.structs import InferStatus, Data

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

import numpy as np


class RunnerCluster(runner.Runner):
    tokenizer: AutoTokenizer
    model: AutoModelForSequenceClassification
    device: torch.device
    sense: int

    def __new__(cls) -> Tuple[InferStatus, Optional[runner.Runner]]:
        if torch.cuda.is_available():
            cls.device = torch.device("cuda")
        else:
            cls.device = torch.device("cpu")
        # Temporary force CPU due to problem with CUDA
        cls.device = torch.device("cpu")
        print(f"Cluster initialization on {cls.device} device...")
        try:
            model_name = "cointegrated/rubert-base-cased-nli-threeway"
            cls.tokenizer = AutoTokenizer.from_pretrained(model_name)
            cls.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        except Exception as exc:
            print(f"Cluster runner initialization failed: {exc}")
            return InferStatus.status_error_init
        print("Done")
        return (InferStatus.status_ok, super(RunnerCluster, cls).__new__(cls))

    def infer(self, data, question) -> Tuple[InferStatus, List[Data]]:
        final_status = InferStatus.status_ok
        answers = [d.corrected for d in data]
        answers_dict = dict(
            map(lambda k, l: (k, l), [i for i in range(0, len(data))], answers)
        )
        while len(answers_dict) > 1:
            index = list(answers_dict.keys())[0]
            answer = answers_dict.pop(index)
            text = f"{question} {answer}"
            label_texts = list(answers_dict.values())
            status, probs = self._predict_zero_shot(text, label_texts)
            if status is not InferStatus.status_ok:
                # Не добавляем ничего в результат, но продолжаем обработку
                final_status = status
                continue
            indices_dict = dict(
                map(lambda k, l: (k, l), list(answers_dict.keys()), probs)
            )
            indices_cluster = [index]
            indices_cluster += self._check_probs(indices_dict)
            cluster_answers = [data[index].corrected]
            for j in range(0, len(data)):
                if j in indices_cluster:
                    cluster_answers.append(data[j].corrected)
            cluster_name = self._get_cluster_name(cluster_answers)
            for j in range(0, len(data)):
                if j in indices_cluster:
                    data[j].cluster = cluster_name
                    if j != index:
                        answers_dict.pop(j)
        if len(answers_dict) == 1:
            index = list(answers_dict.keys())[0]
            answer = answers_dict.pop(index)
            data[index].cluster = answer
        return [final_status, data]

    def _predict_zero_shot(
        self, text, label_texts, label="entailment", normalize=False
    ) -> Tuple[InferStatus, Optional[str]]:
        # Prepare input
        try:
            tokens = self.tokenizer(
                [text] * len(label_texts),
                label_texts,
                truncation=True,
                return_tensors="pt",
                padding=True,
            )
        except Exception as exc:
            print(f"ERROR: cluster runner input preparing failed: {exc}")
            return InferStatus.status_error_prepare
        # Infer
        try:
            with torch.inference_mode():
                result = torch.softmax(
                    self.model(**tokens.to(self.model.device)).logits, -1
                )
        except Exception as exc:
            print(f"ERROR: cluster runner infer failed: {exc}")
            return InferStatus.status_error_infer
        # Output
        proba = result[:, self.model.config.label2id[label]].cpu().numpy()
        if normalize:
            proba /= sum(proba)
        return (InferStatus.status_ok, proba)

    def _check_probs(self, indices_dict) -> List[int]:
        res = []
        for key, value in indices_dict.items():
            if value >= self.sense:
                res.append(key)
        return res

    def _get_cluster_name(self, cluster_answers) -> str:
        lens = [len(ans) for ans in cluster_answers]
        return cluster_answers[np.argmin(lens)]
