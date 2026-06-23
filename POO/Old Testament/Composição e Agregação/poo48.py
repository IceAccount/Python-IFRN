class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class biblioteca:
    def __init__(self,nome):
        self.nome = nome
        self.livros = []
    def adicionarlivros(self, Livro):
        self.livros.append(Livro)
    def listar_livros(self):
        for Livro in self.livros:
            print(f"esse é o livro {Livro.titulo} e o autor é {Livro.autor}.")


livro1 = Livro("cavalo voadores", "Faca de Sacolíss")
livro2 = Livro("Diário de um caçador", "John Winchester")

biblioteca1 = biblioteca("Casa do livro")

biblioteca1.adicionarlivros(livro1)
biblioteca1.adicionarlivros(livro2)

biblioteca1.listar_livros()
