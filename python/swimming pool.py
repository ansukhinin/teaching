# Яша плавал в бассейне размером N × M метров и устал. В этот момент он обнаружил, что находится на расстоянии x метров от одного из длинных бортиков (не обязательно от ближайшего) и y метров от одного из коротких бортиков. Какое минимальное расстояние должен проплыть Яша, чтобы выбраться из бассейна на бортик? Программа получает на вход числа N, M, x, y. Программа должна вывести число метров, которое нужно проплыть Яше до бортика.

N,M,x,y = int(input()), int(input()), int(input()), int(input())

if (N < M):
    if N-x <= x: x=N-x
    if M-y <= y: y= M-y
else:
    if M-x <= x: x=M-x
    if N-y <= y: y= N-y

if x<=y: 
    print(x)
else:
    print(y)

 #  решение разработчиков
n = int(input())
m = int(input())
x = int(input())
y = int(input())
# n, m = min(n, m), max(n, m)
if n > m:
    n, m = m, n
if x >= n / 2:
    x = n - x
if y >= m / 2:
    y = m - y
# print(min(x, y))
if x < y:
    print(x)
else:
    print(y)
