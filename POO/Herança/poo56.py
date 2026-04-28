class Nadador:
    def __init__(self):
        self.nome = 'nome'
    def mover(self):
        print("ELE NADA!!!!!!!!!!!")
class Corredor:
    def __init__(self):
        pass
    def mover(self):
        print("ELE CORRE")
class triatleta(Nadador,Corredor):
    def __init__(self):
        super().__init__()
    def mover(self):
        return super().mover()