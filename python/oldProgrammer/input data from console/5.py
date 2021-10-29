'''
Наконец еще одна проблема, а вдруг среди набора чисел есть не числовые символы. 
Ну здесь уже все просто: нужно в начале получить список строк, а потом все тщательно проверить
'''
#!/usr/bin/python3
nt = list(map(str, input().split()))
fl = 0
for i in range(len(nt)):
    if not nt[i].isdigit():
        fl =  1
        break
    else:
        nt[i] = int(nt[i])
if not fl:
    print(nt)
else:
    print("Ошибка ввода")
    
