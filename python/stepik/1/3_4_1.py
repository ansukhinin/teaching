"""
Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

Файл с данными: Crimes.csv
"""
import csv
from collections import Counter

with open('Crimes.csv') as file:
    reader = csv.reader(file)
    data = list(reader)[1:]
    crimes = list(zip(*data))[5]
    crime_counts = Counter(crimes)
    print(crime_counts.most_common(1))