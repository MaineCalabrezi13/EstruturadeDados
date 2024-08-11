def SomarNumeros(num):
    somar=sum(ListNum)
    return somar

ListNum=[]
ListSoma=[]
NumDigitar=int(input("Deseja digitar quantos números: "))
for i in range(1,NumDigitar+1):
    numeros=int(input("Digite número: "))
    ListNum.append(numeros)
    SomarNumeros(ListNum)
    
print("Números da lista: ",ListNum,"\nSoma da lista: ",SomarNumeros(numeros))
