def contar_digitos(numero, posicao):
    numero_str = str(numero)
    if posicao == len(numero_str):
        return 0
    
    return 1 + contar_digitos(numero, posicao + 1)

numero = 12345
total_digitos = contar_digitos(numero, 0)
print(f"Total de dígitos: {total_digitos}")