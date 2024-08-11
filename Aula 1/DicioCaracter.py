def Cont_caracter(caracter):
    DicLetras.update({caracter:len(caracter)})
    
DicLetras={}

NumDigitar = int(input("Deseja digitar quantas palavras: "))
for i in range(1,NumDigitar+1):
    palavra = input("Digite uma palavra: ").upper()
    Cont_caracter(palavra)
print("Palavras: ",DicLetras)
