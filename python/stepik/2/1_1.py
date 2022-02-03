""" парсим html страницу. надо найти количество упоминаний С++ на странице
ищем в гугле по запросу python 3 download page
находим сайт https://stackoverflow.com
и копируем оттуда нужный код и работаем с ним"""

from urllib.request import urlopen
html = urlopen("https://ru.wikipedia.org/wiki/Python").read().decode('utf-8')
s = str(html) # преобразуем html в str для последущей работы как со строкой
print(s.count("C++"))


