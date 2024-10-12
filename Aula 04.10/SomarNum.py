def somar_lista(lista, posi=0):
    if posi >= len(lista):
        return 0
    else:
        return lista[posi]+somar_lista(lista, posi + 1)
    
resul = somar_lista([1,2,3,4,5])
print(f"Soma dos números: {resul}")