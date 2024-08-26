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
            for i in range(posicao,self.ultima_posicao + 1):
                if i == self.ultima_posicao:
                    self.ultima_posicao = self.ultima_posicao - 1
                else:
                    self.valores[i] = self.valores[i+1]







meuVetor = VetorNaoOrdenado(5)
meuVetor.inserir("M")
meuVetor.inserir("A")
meuVetor.inserir("I")
meuVetor.inserir("N")
meuVetor.inserir("E")
meuVetor.imprimir()
print("\nPesquisa")
print("Letra E: ",meuVetor.pesquisar("E"))
print("Letra N: ",meuVetor.pesquisar("N"))
print("Letra M: ",meuVetor.pesquisar("M"))
print("\nApós Exclusão")
meuVetor.excluir("M")
meuVetor.excluir("I")
meuVetor.excluir("E")
meuVetor.imprimir()