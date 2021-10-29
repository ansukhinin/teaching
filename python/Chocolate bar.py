#Шоколадка имеет вид прямоугольника, разделенного на n×m долек. Шоколадку можно один раз разломить по прямой на две части. Определите, можно ли таким образом отломить от шоколадки часть, состоящую ровно из k долек. Программа получает на вход три числа: n, m, k и должна вывести YES или NO.

n,m,k = int(input()), int(input()), int(input())
k1= n*m #общее кол-во

if k < k1:
    if n == k or m == k: print ('YES')
    elif (k1 - k) == n or (k1 - k) == m: print ('YES')
    elif k % n == 0 and ( k // n) < m: print('YES')
    elif k % m == 0 and ( k // m) < n: print('YES')
    else:
        print ('NO')
else:
    print ('NO')


# решение другое

n,m,k = int(input()), int(input()), int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')