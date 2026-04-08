from dataclasses import dataclass

@dataclass
class Jogador:
    Nome: str
    Posição: str

@dataclass
class time:
    Nome: str
    Lista: Jogador
    def listar_jogadores(self):
        print(f"Todos os jogadores que estão no time:{self.Lista.Nome}")



Jogador1 = Jogador("Carlos", "Costa quadrada")
time1 = time("Vasco", Jogador1)

time1.listar_jogadores()