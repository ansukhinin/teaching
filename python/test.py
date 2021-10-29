
def fun_n(n):
    if n>2:
        return n+fun_n(n-1)-fun_n(n-2)
    else:
        return 2


print(fun_n(6))
    
