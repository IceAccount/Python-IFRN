from dataclasses import dataclass

@dataclass
class Jogador:
    Nome: str
    Posição: str

class time:
    def __init__(self,nome):
        self.Nome = nome
        self.jogadores = []
    def adicionarjogadores(self, Jogador):
        self.jogadores.append(Jogador)
    def listar_jogadores(self):
         for jogador in self.jogadores:
            print(f"Jogador é {jogador.Nome} jogando no {jogador.Posição}")

Jogador1 = Jogador("Carlos", "Costa quadrada")
jogador2 = Jogador("Verlos", "Costa verde")
time1 = time("Vasco")
time1.adicionarjogadores(Jogador1)
time1.adicionarjogadores(jogador2)

time1.listar_jogadores()