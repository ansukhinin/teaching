#По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов
n = int(input())
s = ''
for i in range(n):
    if i< n+1:
        s=s+str(i+1)
        print(s)

# teacher
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, sep='', end='')
    print()
