class Controlavel:
    def __init__(self):
        pass
    def mover(self):
        pass
class Jogador(Controlavel):
    def __init__(self, nome):
        self.nome = nome
    def mover(self):
        print(f"Jogador {self.nome} se movendo")
class Volante(Controlavel):
    def mover(self):
        print("Volante girando")
j1 = Jogador("IceAccount")
v1 = Volante()
j1.mover()
v1.mover()