class Livro: 
    def __init__ (self, titulo, autor): 
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def exibirDetalhes(self):
        if self.disponivel:
            disponibilidade = "Disponivel"
        else:
            disponibilidade = "Indisponivel"
        print("Titulo: ",self.titulo,"\nAutor: ",self.autor,"\nDisponivel: ",disponibilidade)

class Usuario: 
    def __init__ (self, nome): 
        self.nome = nome
        self.livrosEmprestados = []
    def emprestarLivro(self,livro):
        if livro.disponivel:
            livro.disponivel = False
            self.livrosEmprestados.append(livro)
            print(self.nome," emprestou o livro ", livro.titulo)
        else:
            print("O livro ",livro.titulo, "Não está disponível")

    def devolverLivro(self,livro):
        if livro in self.livrosEmprestados:
            livro.disponivel = True
            self.livrosEmprestados.remove(livro)
            print(self.nome," devolveu o livro ", livro.titulo)
        else:
            print("O livro ",livro.titulo, "não existe")
    

class Biblioteca: 
    def __init__ (self, nome): 
        self.nome = nome
        self.livros = []
    
    def adicionarLivro(self,livro):
        self.livros.append(livro)
        print(f"O livro: ",livro.titulo)

    def exibirLivrosDisponiveis(self):
        print(f"Livros disponíveis na biblioteca:")
        livros_disponiveis = [livro for livro in self.livros if livro.disponivel]
        if livros_disponiveis:
            for livro in livros_disponiveis:
                livro.exibirDetalhes()
        else:
            print("Nenhum livro disponível.")

livro1 = Livro("Marley e Eu", "John Grogan")
livro2 = Livro("A Culpa é Das Estrelas", "John Green")
livro3 = Livro("A Bela e a Fera", "Gabrielle-Suzanne Barbot")
biblioteca = Biblioteca("Biblioteca Central")
usuario1 = Usuario("Maine")
usuario2 = Usuario("Agnes")

print("Adicionar livros a biblioteca")
biblioteca.adicionarLivro(livro1)
biblioteca.adicionarLivro(livro2)
biblioteca.adicionarLivro(livro3)
print()

biblioteca.exibirLivrosDisponiveis()
print()
usuario1.emprestarLivro(livro1)
usuario1.emprestarLivro(livro2)
print()
biblioteca.exibirLivrosDisponiveis()
print()
usuario1.devolverLivro(livro1)
print()
biblioteca.exibirLivrosDisponiveis()

