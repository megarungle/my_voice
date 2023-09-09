from typing import Dict, List
from pathlib import Path
from enum import Enum
from dataclasses import dataclass

import json


@dataclass
class DatasetAnswer:
    theme: str
    answer: str
    sentiment: str


class DatasetSentiments(Enum):
    negatives = "negatives"
    neutrals = "neutrals"
    positives = "positives"


def parse_dataset_json(
    json_dataset: Path,
) -> Dict[DatasetSentiments, List[DatasetAnswer]]:
    """Read json dataset and returns all individual answer by sentiment group"""
    with open(json_dataset, "r", encoding="utf-8-sig") as file:
        data = json.load(file)

    sentiments = {
        DatasetSentiments.positives.value: [],
        DatasetSentiments.negatives.value: [],
        DatasetSentiments.neutrals.value: [],
    }

    for i in data["answers"]:
        sentiments[i["sentiment"]].append(
            DatasetAnswer(
                theme=i["cluster"], answer=i["answer"], sentiment=i["sentiment"]
            )
        )

    return sentiments
