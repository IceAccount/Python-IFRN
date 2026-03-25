class fantasma:
    def __init__(self, tipo, morte):
        self.tipo = tipo
        self.morte = morte
    def __str__(self):
        return f"""
        ----------
        sou um {self.tipo}
        e eu morri {self.morte}
        ----------
        """
    def assustar(self):
        print("Boo!!👻")

Sadako = fantasma("Onryo", "Jogada em poço")

Jason = fantasma("Revenant", "Afogado")

Lauany = fantasma("Oni", "Se cedeu a roblox")

print(Sadako)