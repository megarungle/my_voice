import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_checkpoint = 'cointegrated/rubert-base-cased-nli-threeway'
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = AutoModelForSequenceClassification.from_pretrained(model_checkpoint)
if torch.cuda.is_available():
    model.cuda()

question = "Что у проектной команды получается хорошо"
answers = [
    "коммуникации",
    "вести проект",
    "взаимодействие с пользователям",
    "взвешенные решения",
    "догонять",
    "клиентоориентированность",
    "коммуницировать с заказчиком",
    "назначать совещания",
    "собирать совещания",
    "настраивать компьютер",
    "не укладываться в срок",
    "переносить сроки",
    "обратная связь",
    "описывать подходы к разработке",
    "принять правильное решение"
]


def predict_zero_shot(text, label_texts, model, tokenizer, label='entailment', normalize=False):
    tokens = tokenizer([text] * len(label_texts), label_texts, truncation=True, return_tensors='pt', padding=True)
    with torch.inference_mode():
        result = torch.softmax(model(**tokens.to(model.device)).logits, -1)
    proba = result[:, model.config.label2id[label]].cpu().numpy()
    if normalize:
        proba /= sum(proba)
    return proba


classes = answers[1:]
res = predict_zero_shot(answers[0], classes, model, tokenizer)
print(res)
