class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.valores = [None] * capacidade
        self.topo = -1

    def pilha_cheia(self):
        return self.topo == self.capacidade - 1

    def pilha_vazia(self):
        return self.topo == -1

    def empilhar(self, valor):
        if self.pilha_cheia():
            print("Erro: Pilha cheia")
            return
        self.topo += 1
        self.valores[self.topo] = valor

    def desempilhar(self):
        if self.pilha_vazia():
            print("Erro: Pilha vazia")
            return None
        valor = self.valores[self.topo]
        self.topo -= 1
        return valor

    def ver_topo(self):
        if not self.pilha_vazia():
            return self.valores[self.topo]
        return -1

    def mostrar_pilha(self):
        if self.pilha_vazia():
            print("Pilha vazia")
            return
        elementos = self.valores[:self.topo + 1]
        print("Pilha:", elementos[::-1])

# Exemplo de uso
capacidade = 5
pilha = Pilha(capacidade)

pilha.empilhar(10)
pilha.empilhar(20)
pilha.empilhar(30)
pilha.mostrar_pilha()  
print("Topo da pilha:", pilha.ver_topo())

valor = pilha.desempilhar()
print("Valor removido:", valor)
pilha.mostrar_pilha() 

pilha.empilhar(40)
pilha.empilhar(50)
pilha.empilhar(60)
pilha.mostrar_pilha()

pilha.empilhar(70)
