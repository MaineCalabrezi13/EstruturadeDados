def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

import random
numeros = [random.randint(0, 10000) for _ in range(1000)]
    
ordenar_numeros = bubble_sort(numeros.copy())
print("Lista ordenada de 1000 números: ")
print(ordenar_numeros)


nomes = ["Maine","Agnes","Gustavo","Agusto","Alexandre","Mimi","Josue"]

ordenar_nomes = bubble_sort(nomes.copy())
print("Lista ordenada de nomes: ")
print(ordenar_nomes)