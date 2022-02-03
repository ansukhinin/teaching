"""
Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов, на которые есть ссылка.

Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность символов, которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть, за исключением случаев с относительными ссылками вида
<a href="../some_path/index.html">.

Сайты следует выводить в алфавитном порядке.

Пример HTML файла:

<a href="http://stepic.org/courses">
<a href='https://stepic.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="ftp://mail.ru/distib" >
<a href="ya.ru">
<a href="www.ya.ru">
<a href="../skip_relative_links">

Пример ответа:

mail.ru
neerc.ifmo.ru
stepic.org
www.ya.ru
ya.ru
"""

import re, requests

res = requests.get((input().strip()))
l = re.findall(r'<a.+href=(?:"|\')(?:[\w-]+://)?(\w[\w.-]+)', res.text)
ans = set(l)
ans = list(ans)
ans.sort()
for i in ans:
    print(i)


# 2
import requests
import re

page = requests.get(input())

url_pattern = re.compile(r'<a.*?href=["|\'](.*?:\/\/)?(\w.*?)([/|:].*)?["|\'].*')
links = sorted(set([link[1] for link in url_pattern.findall(page.text)]))
print(*links, sep='\n')


# 3
import re
import requests

resp = requests.get(input()).text
sites = set()
for site in re.findall(r'<a.*?href=".*?:\/\/((?:\w|-)+(?:\.(?:\w|-)+)+)', resp):
    sites.add(site)

for site in sorted(sites):
    print(site)

# 4
import requests
import re

pattern = r'<a\s.*?\bhref\s*?=\s*?([\'\"])(\w+://)?(\w.*?)(:\d{1,5})?(/.*?)*\1.*?>.*'
# <a\s.*?\bhref\s*?=\s*?([\'\"]) от начала тега <a до значения атрибута href
# (\w+://)? протокол (1 или 0 вхождение)
# (\w.*?) искомый адрес сайта, начинается с буквы/числа (\w), чтобы отсечь '..'
# (:\d{1,5})? порт (1 или 0 вхождение)
# (/.*?)* относительный путь на сервере (0 или много вхождений)
# \1 закрывающая кавычка атрибута href
# .*?>.* символы до закрывающей скобки тега a, скобка >, остаток строки после тега <a>

resp = requests.get(input().strip())
if resp.status_code == 200:
    l = list(set([match.group(3) for match in re.finditer(pattern, resp.text)]))
    l.sort()
    print(*l, sep='\n')