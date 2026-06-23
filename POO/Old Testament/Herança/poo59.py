class Motor:
    def __init__(self, potencia):
        self.potencia = potencia
    def ligar_motor(self):
        print(f"o motor a potencia de {self.potencia} cavalos ta ligando")
class Eletrico:
    def __init__(self, bateria):
        self.bateria = bateria
    def carregar(self):
        print("ta carregando")
class combustao:
    def __init__(self, tanque):
        self.tanque = tanque
    def abastecer(self):
        print("ta enchendo")

class CarroEletrico(Motor, Eletrico):
    def __init__(self):
        self.nome = 'carro'
    def ligar_motor(self):
        return super().ligar_motor()
    def carregar(self):
        return super().carregar()

class carrohibrido(Motor, Eletrico, combustao):
    def __init__(self):
        self.tipo = "hibrido"
    def ligar_motor(self):
        return super().ligar_motor()
    def abastecer(self):
        return super().abastecer()
    def carregar(self):
        return super().carregar()