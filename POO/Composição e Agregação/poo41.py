class cidade:
    def __init__(self, nome):
        self.nome = nome
class pessoa:
    def __init__(self, nome, cidade):
        self.nome = nome
        self.cidade = cidade
class animal:
    def __init__(self, nome, dono):
        self.nome = nome
        self.dono = dono
    def dados(self):
        print("Animal:", self.nome)
        print("Dono:", self.dono.nome)
        print("Cidade:", self.dono.cidade.nome)

cidade1 = cidade("Ceará")

humano1 = pessoa("Lauany", cidade1)

animal1 = animal("Sol", humano1)

animal1.dados()