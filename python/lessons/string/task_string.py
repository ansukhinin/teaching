#Написать программу корректности ввода телефонного номера по шаблону:
#x(xxx)xxxxxx
#где x – любая цифра от 0 до 9. Данные представлены в виде строки.

while not input('Введите номер телефона:').isdigit():
    print ("в номере только цифры!")

print ('Ok')
print('***')

#Написать программу изменения строки
#"2+3+6.7 + 82 + 5.7 +1"
#на строку, в которой все «+» заменены на «-» и удалены все пробелы

line="2+3+6.7 + 82 + 5.7 +1"
print(line)
print(line.replace(" ","").replace("+","-"))

'''
Написать программу вывода чисел 0; -100; 5.6; -3 в виде столбца:
	0
	-100
	5.6
	-3
в котором все строки выровнены по правому краю (подсказка: воспользуйтесь методом rjust).
'''
number=[0, -100, 5.6, -3]
width=str(number[0])
for n in number: #определяем ширину столбца по наибольшему по количеству знаков
    if len(str(n))> len(width):#ищем самый широкий
        width=str(n)
for n in number: #выводим
    print(str(n).rjust(len(width)))
print('***')    


#4. В строке "abrakadabra" найдите все индексы подстроки «ra» и выведите их (индексы) в консоль.
line="abrakadabraghrahnfgraghra"
idx=line.index("ra")
print(idx)
print(len(line))
while idx <=len(line):
    idx+=2
    if idx+2 >= len(line): break
    idx=line.index("ra",idx)
    print(idx)


    
