'''
Что если требуется обработать несколько чисел, расположенных в одной строке
и отделенных друг от друга пробелами. Ну вот как то так, например:

2 7 9

В Python есть замечательная функция map. Она служит для обработки некоторого
набора данных. Поэтому можно написать так (3.py)


Метод split() служит нам для того, чтобы разбить строку на элементы,
отделенные друг от друга пробелами.
'''
#!/usr/bin/python3
n, m = map(int, input().split())
print(n, m)
