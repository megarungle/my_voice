from typing import List, Dict
from collections import namedtuple

from transformers import pipeline

Sentiment = namedtuple("Sentiment", ["label", "score"])

def get_sentiment(cluster: str) -> Sentiment:
    sentiment_model:List[Dict] = pipeline(model="seara/rubert-tiny2-russian-sentiment")
    return Sentiment(**sentiment_model(cluster)[0])


if __name__ == "__main__":
    print(get_sentiment("убивать детей топором"))
