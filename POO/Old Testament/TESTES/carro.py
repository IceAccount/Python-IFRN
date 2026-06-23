class carro:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def mostrar_dados(self):
        print(self.marca)
        print(self.modelo)
        print(self.ano)

honda = carro("honda","civic",2010)
honda.mostrar_dados()
      