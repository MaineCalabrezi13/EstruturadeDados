class Livro: 
    def __init__ (self, titulo, autor): #Declarar "variaveis", sendo  obrigatorio o self
        self.titulo = titulo
        self.autor = autor
        #self.disponivel = disponivel

        #if self.autor == True:
           # self.lista_disponivel = [self.disponivel]

class Usuario: 
    def __init__ (self, nome, LivrosDisponiveis): #Declarar "variaveis", sendo  obrigatorio o self
        self.nome = nome
        self.LivrosDisponiveis = [LivrosDisponiveis]

class Biblioteca: 
    def __init__ (self, nome, livros): #Declarar "variaveis", sendo  obrigatorio o self
        self.nome = nome
        self.livros = [livros]

class Livraria:
    def __init__(self):
        self.lista_livros = []
    
    def exibir_Detalhes(self,livro):
        self.lista_livros.append(livro)
    
    def adicionar_Livro(self,livro):
        self.lista_livros.append(livro)
    
    def livro_disponi(self,livrodispon):
        self.lista_livros.append(livrodispon)

livro1 = Livro("Pequeno Principe", "Maine")
livro2 = Livro("Joao e Maria", "Agnes")
livro3 = Livro("Programação I", "Augusto")
livro4 = Livro("Programação II", "Gustavo")

livraria_do_site = Livraria()
livraria_do_site.adicionar_Livro(livro1)
livraria_do_site.adicionar_Livro(livro2)
livraria_do_site.adicionar_Livro(livro3)
livraria_do_site.adicionar_Livro(livro4)

print("Total da compra: R$ ",
    livraria_do_site.adicionar_Livro())

