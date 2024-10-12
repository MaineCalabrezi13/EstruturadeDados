def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        marcado = array[i]
        j = i - 1
        while j >= 0 and marcado < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = marcado
    return array

import random
numeros = [random.randint(0, 10000) for _ in range(1000)]
    
ordenar_numeros = insertion_sort(numeros.copy())
print("Lista ordenada de 1000 números: ")
print(ordenar_numeros)


nomes = ["Maine","Agnes","Gustavo","Agusto","Alexandre","Mimi","Josue"]

ordenar_nomes = insertion_sort(nomes.copy())
print("Lista ordenada de nomes: ")
print(ordenar_nomes)