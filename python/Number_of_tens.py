﻿# Дано натуральное число. Найдите число десятков в его десятичной записи.
print (int(input())%100//10)

# разработчики
n = int(input())
print(n // 10 % 10)
