from transformers import pipeline


def get_sentiment(cluster: str):
    sentiment_model = pipeline(model="seara/rubert-tiny2-russian-sentiment")
    return sentiment_model(cluster)


if __name__ == "__main__":
    print(get_sentiment("убивать детей топором"))
