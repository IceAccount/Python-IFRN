class fantasma:
    def __init__(self, tipo):
        self.tipo = tipo
    def assustar(self):
        print("Boo!!👻")

Sadako = fantasma("Onryo")

Jason = fantasma("Revenant")

Lauany = fantasma("Oni")

print(Sadako.tipo)

Sadako.assustar()