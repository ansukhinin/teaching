# В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
# Во второй строке дано одно число days -- число дней.
# Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней, равное days.
import datetime

year, month, day = map(int, input().split()) # Input().split() - разбить прочитанную строку по пробельным символам на строки, получится список строк
# map(функция, последовательность) - применить функцию к каждому элементу последовательности, вернуть полученную последовательность
d = datetime.date(year, month, day)
delta = datetime.timedelta(days=int(input())) # вводим количество дней
result = d + delta
print(result.year, result.month, result.day) # из полученной даты возвращаем отдельно год-месяц-день

# еще варианты
import datetime

r = (int(i) for i in input().split())
newdate = datetime.date(*r) + datetime.timedelta(int(input()))
print(newdate.year, newdate.month, newdate.day)

#
from datetime import date, timedelta

d = date(*[int(i) for i in input().split()]) + timedelta(days = int(input()))
print(d.year, d.month, d.day)

#
import datetime
print(str(datetime.date(*list(map(int, input().split()))) + datetime.timedelta(int(input()))).replace('-0', ' ').replace('-', ' '))

#
from datetime import date, timedelta

x = date(*map(int, input().split())) + timedelta(days=int(input()))

print(x.year, x.month, x.day)