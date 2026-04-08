from dataclasses import dataclass

@dataclass
class Comodo:
    nome: str
    tamanho: str

@dataclass
class casa:
    lista_de_comodos: Comodo