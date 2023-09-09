import torch
from transformers import GPT2Tokenizer, GPT2Model, pipeline
from sklearn.cluster import KMeans
from collections import Counter
import nltk
nltk.download('punkt')



# Загрузка предварительно обученной модели и токенизатора
model_name = "gpt2"  # Можно выбрать другую модель, например, "gpt2-medium", "gpt2-large", "gpt2-xl"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Устанавливаем токен для заполнения (padding token)
tokenizer.pad_token = tokenizer.eos_token

# Ваши ответы
#text = ["исламская религиозная система", "бойцовский клуб", "бокс", "ислам", "христианство", "никита пупсечник", "христианская религиозная система"]
text = ["яблоко", "говно", "груша", "пасечник", "говно яблоко", "арбуз", "ребенок", "украина"]
# Токенизация текста и преобразование в тензор
input_ids = tokenizer(text, padding=True, truncation=True, return_tensors="pt")

# Получение вывода модели
model = GPT2Model.from_pretrained(model_name)
with torch.no_grad():
    output = model(**input_ids)

# Вывод модели содержит информацию о скрытом состоянии (hidden states) и/или классификации, в зависимости от модели.
# Для простоты, можно использовать среднее значение скрытого состояния для классификации.
mean_hidden_state = output.last_hidden_state.mean(dim=1)



# Задайте количество кластеров
num_clusters = 3  # Вы можете выбрать другое количество

# Создайте объект KMeans и выполните кластеризацию
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
clusters = kmeans.fit_predict(mean_hidden_state)

# clusters теперь содержит метки кластеров для каждого ответа
# Вы можете использовать эти метки для группировки ответов

print(clusters)

cluster_dict = {}
for i, cluster_label in enumerate(clusters):
    if cluster_label not in cluster_dict:
        cluster_dict[cluster_label] = []
    cluster_dict[cluster_label].append(text[i])  # text - ваш список ответов

print(cluster_dict)

#
# # Определение общей темы для каждой группы
# for cluster_label, cluster_responses in cluster_dict.items():
#     # Объедините все тексты в группе
#     cluster_text = " ".join(cluster_responses)
#
#     # Разбейте текст на токены (слова)
#     tokens = nltk.word_tokenize(cluster_text)
#
#     # Посчитайте частоту встречаемости слов
#     word_counts = Counter(tokens)
#
#     # Найдите наиболее часто встречающиеся слова
#     most_common_words = word_counts.most_common(5)  # Например, выберите топ-5 слов
#
#     print(f"Cluster {cluster_label}: Most common words: {most_common_words}")

from gensim import corpora
from gensim.models import LdaModel


# Ваши слова
words = []
for i in cluster_dict:
    words.append(cluster_dict[i])

# Создание словаря
dictionary = corpora.Dictionary(words)

# Построение корпуса
corpus = [dictionary.doc2bow(word_list) for word_list in words]

# Модель LDA
num_topics = 3  # Задайте количество тем
lda = LdaModel(corpus, num_topics=num_topics, id2word=dictionary)

# Вывод тем
for i, topic in lda.show_topics():
    print(f"Topic {i}: {topic}")