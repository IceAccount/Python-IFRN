class fantasma:
    def __init__(self, tipo, morte):
        self.tipo = tipo
        self.morte = morte
    def assustar(self):
        print("Boo!!👻")

Sadako = fantasma("Onryo", "Jogada em poço")

Jason = fantasma("Revenant", "afogado")

Lauany = fantasma("Oni", "tesoura demais")

print(Lauany.tipo)
print(Lauany.morte)

Sadako.assustar()