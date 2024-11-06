class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def mostra_no(self):
        print(self.valor)


class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        novo = No(valor)
        if self.raiz is None:
            self.raiz = novo
        else:
            atual = self.raiz
            while True:
                pai = atual
                # Esquerda
                if valor < atual.valor:
                    atual = atual.esquerda
                    if atual is None:
                        pai.esquerda = novo
                        return
                # Direita
                else:
                    atual = atual.direita
                    if atual is None:
                        pai.direita = novo
                        return

    def pesquisar(self, valor):
        atual = self.raiz
        while atual is not None and atual.valor != valor:
            if valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita
        return atual

    # Travessia pré-ordem (Raiz, esquerda, direita)
    def pre_ordem(self, no):
        if no is not None:
            print(no.valor)
            self.pre_ordem(no.esquerda)
            self.pre_ordem(no.direita)

    # Travessia em-ordem (Esquerda, raiz, direita)
    def em_ordem(self, no):
        if no is not None:
            self.em_ordem(no.esquerda)
            print(no.valor)
            self.em_ordem(no.direita)

    # Travessia pós-ordem (Esquerda, direita, raiz)
    def pos_ordem(self, no):
        if no is not None:
            self.pos_ordem(no.esquerda)
            self.pos_ordem(no.direita)
            print(no.valor)

    def excluir(self, valor):
        if self.raiz is None:
            print("A árvore está vazia")
            return False

        atual = self.raiz
        pai = self.raiz
        e_esquerda = True

        while atual is not None and atual.valor != valor:
            pai = atual
            if valor < atual.valor:
                e_esquerda = True
                atual = atual.esquerda
            else:
                e_esquerda = False
                atual = atual.direita

        if atual is None:
            return False

        # Caso 1: O nó a ser apagado é uma folha
        if atual.esquerda is None and atual.direita is None:
            if atual == self.raiz:
                self.raiz = None
            elif e_esquerda:
                pai.esquerda = None
            else:
                pai.direita = None

        # Caso 2: O nó a ser apagado não possui filho na direita
        elif atual.direita is None:
            if atual == self.raiz:
                self.raiz = atual.esquerda
            elif e_esquerda:
                pai.esquerda = atual.esquerda
            else:
                pai.direita = atual.esquerda

        # Caso 3: O nó a ser apagado não possui filho na esquerda
        elif atual.esquerda is None:
            if atual == self.raiz:
                self.raiz = atual.direita
            elif e_esquerda:
                pai.esquerda = atual.direita
            else:
                pai.direita = atual.direita

        # Caso 4: O nó possui dois filhos
        else:
            sucessor = self.get_sucessor(atual)
            if atual == self.raiz:
                self.raiz = sucessor
            elif e_esquerda:
                pai.esquerda = sucessor
            else:
                pai.direita = sucessor
            sucessor.esquerda = atual.esquerda

        return True

    def get_sucessor(self, no):
        pai_sucessor = no
        sucessor = no
        atual = no.direita

        while atual is not None:
            pai_sucessor = sucessor
            sucessor = atual
            atual = atual.esquerda

        if sucessor != no.direita:
            pai_sucessor.esquerda = sucessor.direita
            sucessor.direita = no.direita

        return sucessor


# Teste do código
if __name__ == "__main__":
    arvore = ArvoreBinariaBusca()
    arvore.inserir(60)
    arvore.inserir(50)
    arvore.inserir(70)
    arvore.inserir(40)
    arvore.inserir(65)
    arvore.inserir(55)
    arvore.inserir(75)

    print("Travessia em pré-ordem:")
    arvore.pre_ordem(arvore.raiz)

    print("\nTravessia em em-ordem:")
    arvore.em_ordem(arvore.raiz)

    print("\nTravessia em pós-ordem:")
    arvore.pos_ordem(arvore.raiz)

    print("\nPesquisando o valor 7:")
    resultado = arvore.pesquisar(7)
    if resultado:
        print("Valor encontrado:", resultado.valor)
    else:
        print("Valor não encontrado")

    print("\nExcluindo o valor 50:")
    arvore.excluir(50)
    print("Travessia em em-ordem após exclusão:")
    arvore.em_ordem(arvore.raiz)
    
    print("\nExcluindo o valor 60:")
    arvore.excluir(60)
    print("Travessia em em-ordem após exclusão:")
    arvore.em_ordem(arvore.raiz)