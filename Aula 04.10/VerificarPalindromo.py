def verificar_palindromo(palavra):
    return palavra == palavra[::-1]

print(verificar_palindromo("radar"))
print(verificar_palindromo("python"))