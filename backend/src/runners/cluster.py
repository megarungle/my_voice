from typing import List, Tuple, Optional

from src.interface import runner
from src.structs import InferStatus, Data

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

import numpy as np
from fuzzywuzzy import process


class RunnerCluster(runner.Runner):
    tokenizer: AutoTokenizer
    model: AutoModelForSequenceClassification
    device: torch.device
    sense: float

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
        values = list(answers_dict.values())
        while len(answers_dict) > 1:
            index = list(answers_dict.keys())[0]
            answer = answers_dict[index]
            text = f"{answer}"
            label_texts = list(answers_dict.values())

            probs = process.extract(answer, label_texts, limit=len(label_texts))
            count = self._check_probs(probs)
            probs = probs[:count]
            indices_cluster = []
            for prob in probs:
                if values.count(prob[0]) == 1:
                    indices_cluster.append(values.index(prob[0]))
                else:
                    for i in range(len(values)):
                        if values[i] == prob[0]:
                            indices_cluster.append(i)

            cluster_answers = [data[x].answer for x in indices_cluster]
            cluster_name = self._get_cluster_name(cluster_answers)

            for i in range(len(indices_cluster)):
                data[indices_cluster[i]].cluster = cluster_name
                if indices_cluster[i] in answers_dict:
                    answers_dict.pop(indices_cluster[i])

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

    def _check_probs(self, probs) -> int:
        for i in range(len(probs)):
            if probs[i][1] < self.sense:
                return i

    def _get_cluster_name(self, cluster_answers) -> str:
        lens = [len(ans) for ans in cluster_answers]
        return cluster_answers[np.argmin(lens)]
