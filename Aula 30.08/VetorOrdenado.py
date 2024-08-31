import numpy as np
class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.vetor = []
        self.valores = np.empty(self.capacidade, dtype=int) #Montar o quadrado da capacidade
    
    def inserir(self,valor):
        if(self.ultima_posicao == self.capacidade-1):
            print("O vetor está cheio!",valor)
            return
        posicao = 0
        #Inserção ordenada
        #Achar onde inserir
        for i in range(self.ultima_posicao + 1):
            posicao = i
            #achou o local p/ inserir
            if (self.valores[i]>valor):
                break

            #é para inserir no final
            if (i == self.ultima_posicao):
                posicao = i+1
        #Aqui é a inserção
        j = self.ultima_posicao
        while(j>=posicao):
            self.valores[j+1] = self.valores[j]
            j-=1
        self.valores[posicao] = valor
        self.ultima_posicao +=1




    def imprimir(self):
        if (self.ultima_posicao == -1):
            print("Vetor vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print('Posição {} | Valor {}'.format(i, self.valores[i]))

    def pesquisa_binario(self, valor):
        limite_inferior = 0
        limite_superior = self.ultima_posicao
        
        while True:
            posicao_atual = int((limite_inferior+limite_superior)/2)
            print("Limite_inferior {} | Limite_superior {} | Posição_atual{}".format(limite_inferior,limite_superior,posicao_atual  ))
            #Encontrou
            if self.valores[posicao_atual] == valor:
                return posicao_atual
            #Passou por tudo e não encontrou
            elif limite_inferior>limite_superior:
                return -1
            #Escolhe um lado e vai
            else:
                #Se é maior, vai para a direita
                if(self.valores[posicao_atual]<valor):
                    limite_inferior=posicao_atual+1
                #Se é menor, vai para a esquerda
                else:
                    limite_superior = posicao_atual-1    


    def pesquisar(self,valor):
        for i in range(self.ultima_posicao + 1):

            #Achou um maior que ele
            if(self.valores[i] > valor):
                return -1
            
            if (self.valores[i] == valor):
                return i
            
        #Pior caso, procurou por tudo e não achou nada
        return -1
        

    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao,self.ultima_posicao):
                self.valores[i] = self.valores[i+1]
                




Vetor = VetorOrdenado(7)
Vetor.imprimir()
Vetor.inserir(9)
Vetor.imprimir()
Vetor.inserir(4)
Vetor.imprimir()
Vetor.inserir(5)
Vetor.imprimir()
Vetor.inserir(8)
Vetor.imprimir()
Vetor.inserir(2)
Vetor.imprimir()
Vetor.inserir(3)
Vetor.imprimir()
Vetor.inserir(1)
Vetor.imprimir()
Vetor.inserir(12)#Vai dar cheio
Vetor.imprimir()
Vetor.pesquisa_binario(19)
print("Pesquisa",Vetor.pesquisar(8))
