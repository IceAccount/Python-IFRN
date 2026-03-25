class fantasma:
    def __init__(self, tipo, morte):
        self.tipo = tipo
        self.morte = morte
    def assustar(self):
        print("Boo!!👻")

Sadako = fantasma("Onryo", "Jogada em poço")

Jason = fantasma("Revenant", "Afogado")

Lauany = fantasma("Oni", "Se cedeu a roblox")

print(Lauany.tipo)
print(Lauany.morte)

Sadako.assustar()