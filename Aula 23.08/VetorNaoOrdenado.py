class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = [''] * capacidade #Montar o quadrado da capacidade
    
    def inserir(self,valor):
        if(self.ultima_posicao == self.capacidade-1):
            print("O vetor está cheio!")
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao]= valor
    
    def imprimir(self):
        if (self.ultima_posicao == -1):
            print("Vetor vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print('Posição {} | Valor {}'.format(i, self.valores[i]))

    def pesquisar(self,valor):
        for i in range(self.ultima_posicao + 1):
            if (self.valores[i]) == valor:
                return i

    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao,self.ultima_posicao):
                self.valores[i] = self.valores[i+1]




meuVetor = VetorNaoOrdenado(4)
meuVetor.imprimir()
meuVetor.inserir(2)
meuVetor.inserir(17)
meuVetor.inserir(7)
meuVetor.inserir(25)
meuVetor.imprimir()
print(meuVetor.pesquisar(17))
print(meuVetor.pesquisar(35))
print(meuVetor.pesquisar(25))
meuVetor.excluir(17)
meuVetor.imprimir()