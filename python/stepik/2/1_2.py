"""
Файл https://stepik.org/media/attachments/lesson/209719/2.html содержит статью с Википедии про язык Python. В этой статье есть теги code, которыми выделяются конструкции на языке Python. Вам нужно найти все строки, содержащиеся между тегами <code> и </code> и найти те строки, которые встречаются чаще всего и вывести их в алфавитном порядке, разделяя пробелами.

Например, если исходный текст страницы выглядел бы так:

<code>a</code>
<a>bracadabr</a>
<code>c</code>
<code>b</code>
<code>b</code>
<code>c</code>
то в ответ надо было бы ввести строку "b c".
"""

import re
from urllib.request import urlopen
from collections import Counter # для подсчета

html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')
a = re.findall((r'<code>(.*?)</code>'), html)
a.sort()
print(Counter(a).most_common(3))
# надо доделать, путь верный