class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.valores = [None] * capacidade
        self.inicio = 0
        self.final = -1
        self.n_elementos = 0

    def fila_cheia(self):
        return self.n_elementos == self.capacidade

    def fila_vazia(self):
        return self.n_elementos == 0

    def enfileirar(self, valor):

        if self.fila_cheia():
            print("Erro: Fila cheia")
            return

        self.final = (self.final + 1) % self.capacidade 
        self.valores[self.final] = valor
        self.n_elementos += 1

    def desenfileirar(self):
        if self.fila_vazia():
            print("Erro: Fila vazia")
            return None

        temp = self.valores[self.inicio]
        self.inicio = (self.inicio + 1) % self.capacidade  
        self.n_elementos -= 1
        return temp

    def primeiro(self):
        """Retorna o valor no início da fila sem removê-lo."""
        if self.fila_vazia():
            return -1
        return self.valores[self.inicio]

    def mostrar_fila(self):
        """Mostra os elementos da fila em ordem."""
        if self.fila_vazia():
            print("Fila vazia")
            return

        elementos = []
        i = self.inicio
        for _ in range(self.n_elementos):
            elementos.append(self.valores[i])
            i = (i + 1) % self.capacidade
        print("Fila:", elementos)

# Exemplo de uso
capacidade = 5
fila = FilaCircular(capacidade)

# Enfileirar elementos
fila.enfileirar(10)
fila.enfileirar(20)
fila.enfileirar(14)

# Mostrar fila
fila.mostrar_fila()

# Mostrar o primeiro elemento
print("Primeiro valor:", fila.primeiro())
# Desenfileirar um elemento
valor = fila.desenfileirar()
print("Valor removido:", valor)

# Mostrar fila após desenfileirar
fila.mostrar_fila()

# Enfileirar mais elementos
fila.enfileirar(38)
fila.enfileirar(50)
fila.enfileirar(25)
# Mostrar fila
fila.mostrar_fila()

# Tentando enfileirar quando a fila está cheia
fila.enfileirar(70)
# Desenfileirar todos os elementos
print("Desenfileirando todos os elementos:")
while not fila.fila_vazia():
    print(fila.desenfileirar())
