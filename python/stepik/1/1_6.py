# Рассмотрим следующее объявление классов

class A:
    pass

class B(A):
    pass

class C:
    pass

class D(C):
    pass

class E(D, C, B):
    pass

#Какие последовательности могут являться корректным порядком разрешения методов для класса E?
print(E.mro())