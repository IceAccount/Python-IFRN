class Motor:
    def __init__(self):
        self.n = 'nome'
        self.potencia = 'potencia'

class Carro:
    def __init__(self,nome):
        self.nome = nome
        self.motor = Motor

class MotorEletrico(Motor):
    def __init__(self):
        super().__init__()
        self.nome = "nomeeletrico"
        self.potencia = "potenciaeletrica"

class CarroEletrico(Carro):
    def __init__(self, nome):
        super().__init__(nome)
        self.motoreletrico = MotorEletrico