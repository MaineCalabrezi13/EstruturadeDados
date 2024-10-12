def triangulo(n, linha=1):
    if linha>n:
        return
    print('*' * linha)
    
    triangulo(n, linha + 1)

triangulo(3)