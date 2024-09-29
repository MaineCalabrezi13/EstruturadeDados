class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

class ListaEncadeadaDupla:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def lista_vazia(self):
        return self.primeiro is None

    def insere_inicio(self, valor):
        novo = No(valor)
        if self.lista_vazia():
            self.ultimo = novo
        else:
            self.primeiro.anterior = novo
            novo.proximo = self.primeiro
        self.primeiro = novo

    def insere_final(self, valor):
        novo = No(valor)
        if self.lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
            novo.anterior = self.ultimo
        self.ultimo = novo

    def excluir_inicio(self):
        if self.lista_vazia():
            return None
        temp = self.primeiro
        if self.primeiro.proximo is None:
            self.ultimo = None
        else:
            self.primeiro.proximo.anterior = None
        self.primeiro = self.primeiro.proximo
        return temp

    def excluir_final(self):
        if self.lista_vazia():
            return None
        temp = self.ultimo
        if self.primeiro.proximo is None:
            self.primeiro = None
        else:
            self.ultimo.anterior.proximo = None
        self.ultimo = self.ultimo.anterior
        return temp

    def excluir_qualquer(self, valor):
        atual = self.primeiro
        while atual is not None and atual.valor != valor:
            atual = atual.proximo
        if atual is None:
            return None
        if atual == self.primeiro:
            self.primeiro = atual.proximo
        else:
            atual.anterior.proximo = atual.proximo
        if atual == self.ultimo:
            self.ultimo = atual.anterior
        else:
            atual.proximo.anterior = atual.anterior
        return atual

    def mostrar_inicio(self):
        atual = self.primeiro
        while atual is not None:
            print(atual.valor, end=' ')
            atual = atual.proximo
        print()

    def mostrar_final(self):
        atual = self.ultimo
        while atual is not None:
            print(atual.valor, end=' ')
            atual = atual.anterior
        print()

    def pesquisar(self, valor):
        if self.lista_vazia():
            return None
        atual = self.primeiro
        while atual is not None and atual.valor != valor:
            if atual.proximo is None:
                return None
            atual = atual.proximo
        return atual


def exercicio_lista_encadeada(nome):
    lista = ListaEncadeadaDupla()


    for char in nome:
        lista.insere_final(char)


    print("Lista do início para o final:")
    lista.mostrar_inicio()


    excluido = lista.excluir_inicio()
    if excluido:
        print(f"\nElemento excluído do início: {excluido.valor}")
    else:
        print("Nenhum elemento para excluir.")
    
    print("Lista após exclusão do primeiro elemento:")
    lista.mostrar_inicio()

    ultimo_char = nome[-1]
    encontrado = lista.pesquisar(ultimo_char)
    if encontrado:
        print(f"\nPesquisa pelo último caractere '{ultimo_char}': Encontrado")
    else:
        print(f"'{ultimo_char}' não encontrado.")

    if len(nome) > 2:
        elemento_aleatorio = nome[1]
        excluido_aleatorio = lista.excluir_qualquer(elemento_aleatorio)
        print(f"\nElemento '{elemento_aleatorio}' excluído da lista: {excluido_aleatorio.valor if excluido_aleatorio else 'Não encontrado'}")

        print("Lista após exclusão do elemento:")
        lista.mostrar_inicio()
    else:
        print("Lista não tem elementos suficientes para excluir.")

nome = "Maine"
exercicio_lista_encadeada(nome)