class Produto: 
    def __init__ (self, nome, preco): #Declarar "variaveis", sendo  obrigatorio o self
        self.nome = nome
        self.preco = preco

class Carrinho:
    def __init__(self):
        self.lista_produtos = []
    
    def adicionar_produto(self,produto):
        self.lista_produtos.append(produto) #Vai adicionar o produto em uma lista 
    
    def remover_produto(self, produto):
        self.lista_produtos.remove(produto)
    
    def calcular_total(self):
        total = 0
        for p in self.lista_produtos:
            total += p.preco
        return total



p1 = Produto("Ar condicionado", 2499.00)
p2 = Produto("Lava e seca (Sansung)",3940.99)
p3 = Produto("Microondas",450.00)
p4 = Produto("Xbox Serie S",3500.00)

carrinho_do_site = Carrinho()
carrinho_do_site.adicionar_produto(p1)
carrinho_do_site.adicionar_produto(p2)
carrinho_do_site.adicionar_produto(p3)
carrinho_do_site.adicionar_produto(p4)

print("Total da compra: R$ ",
    carrinho_do_site.calcular_total())

carrinho_do_site.remover_produto(p4)
print("Agora a compra deu: R$ ",
    carrinho_do_site.calcular_total())


