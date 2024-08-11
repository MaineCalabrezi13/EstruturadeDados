def numeros_pares(lista):
    for num in lista:
        if (num%2==0):
            ListPar.append(num)
    return ListPar
ListNum=[]
ListPar=[]

NumDigitar = int(input("Quantos números deseja digitar: "))

for i in range(1,NumDigitar+1):
    Numeros = int(input("Digite um número: "))
    ListNum.append(Numeros)
    
print("Lista de números digitados: ",ListNum,"\nLista de números pares: ",numeros_pares(ListNum))
    