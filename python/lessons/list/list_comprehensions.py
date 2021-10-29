# нам нужно создать список, состоящий из квадратов чисел,
# определенных от 0 до N-1.
# это можно было бы реализовать так:

A=[]
N=10
for x in range(N):
     A.append(x**2)
 
print(A)

# вариант 2:
N=10
A = [x**2 for x in range(N)]
print(A)

print('***')

# Теперь немного усложним этот пример, и предположим, что нам нужно
# создать список только из четных чисел. вариант 1:

A=[]
N=10
for x in range(N):
     if x%2 == 0:
          A.append(x**2)
print(A)

# А через list comprehensions это записывается следующим образом:

N=10
A = [x**2 for x in range(N) if x%2 == 0]
print(A)

print('***')

# вариант со строками
cities = ["Москва", "Тверь", "Рязань", "Ярославль", "Владимир"]
print(cities)
A = [city for city in cities if len(city) < 7]
print(A)
