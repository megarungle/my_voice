
# Ваши тексты
texts = ["исламская религиозная система", "бойцовский клуб", "бокс", "ислам", "христианство", "никита пупсечник", "христианская религиозная система"]
 # Список ваших текстов
#labels = ["религия", "спорт", "прочее"]  # Список меток классов (0 - не религиозная система, 1 - религиозная система)

from transformers import RobertaTokenizer, RobertaModel, AutoTokenizer, AutoModel, pipeline
import torch
import numpy as np


pipe = pipeline("feature-extraction", model="DeepPavlov/rubert-base-cased")
# Загрузка предварительно обученной модели и токенизатора
tokenizer = AutoTokenizer.from_pretrained("DeepPavlov/rubert-base-cased")
model = AutoModel.from_pretrained("DeepPavlov/rubert-base-cased")

# Преобразование текстов в эмбеддинги
embeddings = []
for text in texts:
    input_ids = tokenizer.encode(text, add_special_tokens=True, max_length=128, padding="max_length", truncation=True, return_tensors="pt")
    with torch.no_grad():
        output = model(input_ids)
    embeddings.append(output.pooler_output.numpy())


from gensim import corpora
from gensim.models import LdaModel

# Преобразование векторов в словарь Gensim
dictionary = corpora.Dictionary(embeddings)

# Построение корпуса
corpus = [dictionary.doc2bow(embedding) for embedding in embeddings]

# Модель LDA
num_topics = 5  # Задайте количество тем
lda = LdaModel(corpus, num_topics=num_topics, id2word=dictionary)

# Вывод слов для каждой темы
for i, topic in lda.show_topics():
    print(f"Topic {i}: {topic}")
