class computador:
    def __init__(self, processador, memoria):
        self.processador = processador
        self.memoria = memoria
class laptop(computador):
    def __init__(self, processador, memoria, bateria):
        super().__init__(processador, memoria, bateria)
        self.processador = processador
        self.memoria = memoria
        self.bateria = bateria
class cabinete(computador):
    def __init__(self, processador, memoria, cabinete):
        super().__init__(processador, memoria, cabinete)
        self.processador = processador
        self.memoria = memoria
        self.cabinete = cabinete
        