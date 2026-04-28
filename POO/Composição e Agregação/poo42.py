from dataclasses import dataclass

@dataclass
class Motor:
    potencia: int
    def ligar(self):
        print(f"Motor de {self.potencia} cavalos ligando")


@dataclass
class Carro:
    modelo: str
    motor: Motor
    def ligar_carro(self):
        print(f"Ligando {self.modelo}...")
        self.motor.ligar()

Samsung = Motor(67670)
john = Carro("Circulos point", Samsung)
john.ligar_carro()