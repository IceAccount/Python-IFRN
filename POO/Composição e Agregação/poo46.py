from dataclasses import dataclass
@dataclass
class comodo:
    nome: str
    tamanho: int
class casa:
    def __init__(self, nome):
        self.nome = nome
        self.comodos = []
    def adicionarsalas(self, comodo):
        self.comodos.append(comodo)
    def listarsalas(self):
        for comodo in self.comodos:
            print(f"essa sala é a {comodo.nome} e tem {comodo.tamanho} metros de largura")

sala1 = comodo("Corredor", 7)
sala7 = comodo("Garagem", 10)

casa1 = casa("Tanglewood 7")
casa1.adicionarsalas(sala1)
casa1.adicionarsalas(sala7)
casa1.listarsalas()