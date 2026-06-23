from dataclasses import dataclass

@dataclass
class Autor:
    Nome: str


@dataclass
class Livro:
    Tipo: str
    autor: Autor
    Historia: str
    def Ler_livro(self):
        print(f"O tipo do livro é {self.Tipo}, quem escreveu é {self.autor.Nome} e a historia é {self.Historia}")


Autor1 = Autor("IceStul")
As_aventuras_serelepes_de_Steve = Livro("ficção", Autor1, "Ele morreu")


As_aventuras_serelepes_de_Steve.Ler_livro()