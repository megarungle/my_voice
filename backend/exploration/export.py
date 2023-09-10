from os import walk
import json
import csv

mypath = '../dataset/labeled/'

header = ['question', 'answer', 'count', 'cluster', 'sentiment', 'corrected']

filenames = next(walk(mypath), (None, None, []))[2]

table = []
for f in filenames:
    with open(mypath + f, 'r', encoding='utf-8-sig') as file:
        print(file)
        data = json.load(file)

    for answer in data['answers']:
        if "corrected" in answer:
            corrected = answer['corrected']
        else:
            corrected = ''

        row = [data['question'], answer['answer'], answer['count'], answer['cluster'], answer['sentiment'],
               corrected]
        table.append(row)


with open('dataset.csv', 'w', encoding='utf-8-sig', newline='') as c:
    writer = csv.writer(c, delimiter=';')
    writer.writerow(header)
    writer.writerows(table)
