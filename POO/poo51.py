class computador:
    def __init__(self, processador, memoria):
        self.processador = processador
        self.memoria = memoria
    def componentes(self):
        print(self.processador)
        print(self.memoria)
class laptop(computador):
    def __init__(self, processador, memoria):
        super().__init__(processador, memoria)
        self.processador = processador
        self.memoria = memoria
        self.bateria = 0
class desktop(computador):
    def __init__(self, processador, memoria):
        super().__init__(processador, memoria)
        self.processador = processador
        self.memoria = memoria
        self.cabinete = ""