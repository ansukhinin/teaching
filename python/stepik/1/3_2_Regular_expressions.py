# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.

# Подключаем (импортируем) модули
# для работы с регулярными выражениями
import re
# для работы с командной строкой
import sys

for line in sys.stdin:     # В цикле считываем строки из командной строки.
    line = line.strip()
    if re.search(r"cat.*cat", line):# Задаем шаблон регулярного выражения.
        print(line)


# Вам дана последовательность строк. Выведите строки, содержащие "cat" в качестве слова.
import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r"\bcat\b", line):
        print(line)


# Вам дана последовательность строк. Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.
import re
import sys

for line in sys.stdin:
    line = line.strip()
    if re.search(r"z...z", line):
        print(line)

# вариант 2
import re, sys
sys.stdout.writelines(filter(re.compile('z...z').search, sys.stdin))

# Вам дана последовательность строк. Выведите строки, содержащие обратный слеш "\﻿".
import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r"\\", line):
        print(line)
# второй вариант                                                                                             
import sys
print(*filter(lambda line: "\\" in line, sys.stdin), sep='')


# Вам дана последовательность строк. Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).
import re
import sys

for line in sys.stdin:
    line = line.strip()
    if re.search(r"\b(\w+)\1\b", line):
        print(line)
# второй вариант
import sys, re
sys.stdout.writelines(filter(re.compile(r"\b(\w+)\1\b").search, sys.stdin))

# Вам дана последовательность строк. В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿ и выведите полученные строки.
import re
import sys

for line in sys.stdin:
    line = line.strip()
    line = re.sub(r"human", "computer", line)
    print(line)
# второй вариант
import re
import sys

print(re.sub(r'human', 'computer', sys.stdin.read()), end='')


# Вам дана последовательность строк. В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен), на слово "argh".
import re
import sys

for line in sys.stdin:
    line = line.strip()
    line = re.sub(r"\ba+\b", "argh", line, count=1, flags=re.IGNORECASE)
    print(line)

# Вам дана последовательность строк. В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв. Буквой считается символ из группы \w.
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r'\b(\w)(\w)', r"\2\1", line))

# Вам дана последовательность строк. В каждой строке замените все вхождения нескольких одинаковых букв на одну букву. Буквой считается символ из группы \w.
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r"(\w)\1+", r'\1', line))

# Введите с клавиатуры список с различными значениями (цифры, слова, символы). Необходимо проверить, есть ли в этом списке два слова подряд и вывести их на экран. Если таких пар нет, то выведите фразу "Мало слов!"

import re
def solution():
    text = input()
    result = re.findall(r'\s+'.join([r'[^\d\s]+']*2), text)
    print(*(result if result else ["Мало слов!"]), sep='\n')
solution()
