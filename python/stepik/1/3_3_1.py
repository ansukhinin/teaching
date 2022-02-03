#  Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
# Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

import re
import urllib.request

a = input()
b = input()

def get_links(url):
    try:
        fp = urllib.request.urlopen(url)
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        fp.close()
        links = re.findall(r'<a.*href="([^"]*)"', mystr)
    except:
        return []
    else:
        return links

def two_steps():
    links1 = get_links(a)

    for link in links1:
        links2 = get_links(link)
        if b in links2:
            return True
    return False

if two_steps():
    print("Yes")
else:
    print("No")



# 2
import requests, re

urls = [input() for cmd in range(2)]
p = 'No'

for i in re.findall(r'<a.*href="(.*)">', requests.get(urls[0]).text):
    if urls[1] in re.findall(r'<a.*href="(.*)">', requests.get(i).text):
        p = 'Yes'
        break

print(p)
