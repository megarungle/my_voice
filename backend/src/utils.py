from typing import Dict, List
from collections import namedtuple, defaultdict
from pathlib import Path

import json


Answer = namedtuple("Answer", ["answer", "sentiment"])

# TODO: Better data structs
def parse_dataset_json(json_dataset: Path) -> Dict[str, Dict[str, List[str]]]:
    with open(json_dataset, 'r', encoding='utf-8-sig') as file:
        data = json.load(file)

    sorted_by_themes: Dict[str, List[Answer]]= defaultdict(list)
    for item in data["answers"]:
        sorted_by_themes[item["cluster"]].append(Answer(item["answer"], item["sentiment"]))

    sentiments = {
        "positives": {},
        "negatives": {},
        "neutrals": {}
    }

    for theme, answers in sorted_by_themes.items():
        for answer in answers:
            if theme in sentiments[answer.sentiment].keys():
                sentiments[answer.sentiment][theme]["answers"].append(answer.answer)
            else:
                sentiments[answer.sentiment][theme] = {"answers": [answer.answer]}
    return sentiments
