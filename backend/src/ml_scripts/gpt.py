import torch
from transformers import AutoTokenizer, AutoModelForMaskedLM
from sklearn.cluster import DBSCAN
import numpy as np

# Ваши ответы
question = "Что у проектной команды получается хорошо"
answers = [
    "вести проект",
    "взаимодействие с пользователям",
    "взвешенные решения",
    "догонять",
    "клиентоориентированность",
    "коммуникации",
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

# Загрузка предварительно обученной модели BERT и токенизатора
model_name = 'ai-forever/ruRoberta-large'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForMaskedLM.from_pretrained(model_name)

# Получение эмбеддингов текстов с использованием BERT
embeddings = []
for answer in answers:
    input_text = f"Вопрос: {question} Ответ: {answer}"
    inputs = tokenizer.encode(input_text, add_special_tokens=True)
    with torch.no_grad():
        outputs = model(**inputs).logits
    embeddings.append(outputs.last_hidden_state.mean(dim=1).squeeze().numpy())

# Кластеризация с DBSCAN
dbscan = DBSCAN(eps=1.25, min_samples=1)  # Параметры могут потребоваться настройки
clusters = dbscan.fit_predict(embeddings)

# Группировка ответов по кластерам
num_clusters = len(set(clusters))
grouped_answers = [[] for _ in range(num_clusters)]
for i, cluster_id in enumerate(clusters):
    grouped_answers[cluster_id].append(answers[i])

# Вывод результатов
for i, group in enumerate(grouped_answers):
    print(f"Группа {i+1}:")
    print(group)
