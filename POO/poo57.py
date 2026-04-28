class Veiculo:
    def __init__(self):
        self.tipo = 'tipo'
    def acelerar(self):
        print("som")
class Carro(Veiculo):
    def __init__(self):
        super().__init__()
        self.tipo = 'carro'
    def acelerar(self):
        print("ram ram")

class Moto(Veiculo):
    def __init__(self):
        super().__init__()
        self.tipo = 'moto'
    def acelerar(self):
        print("vrum vrum")
    
Civic = Carro()
Vespa = Moto()

Civic.acelerar()
Vespa.acelerar()