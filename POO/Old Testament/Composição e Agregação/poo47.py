from dataclasses import dataclass

@dataclass
class Processador:
    modelo: str
    velocidade: int
@dataclass
class Memoria:
    capacidade: int
@dataclass
class computador:
    nome: str
    processador: Processador
    memoria: Memoria
    def exibir_configurações(self):
        print(f"o processador do pc é {self.processador.modelo} com a velocidade {self.processador.velocidade} e com uma memoria de {self.memoria.capacidade}")

p1 = Processador("RTX", 5060)
m1 = Memoria(8800)

pc1 = computador("pc gamerrrrrr", p1, m1)
pc1.exibir_configurações()