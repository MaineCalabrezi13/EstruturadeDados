def ColocarLista(elementos):
    for i in range(0,5):
        elementos=input("Digite algo: ").upper()
        Lista.append(elementos)
        
Lista=[]
print("Lista atual: ",Lista)
ColocarLista(Lista)
print("Lista completa do que você digitou: ",Lista)