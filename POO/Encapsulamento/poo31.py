class estudande:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.__creditos = 1

    def detalhar(self):
        print(self.id)
        print(self.nome)
        print(self.__creditos)

    def adicionar_creditos(self):
        while True:
            creditonovo = int(input("Coloque os creditos! "))
            if creditonovo == 0:
                print("tente novamente!")
            else:
                self.__creditos += creditonovo
                break
lucca = estudande(0,"Lucca")
lucca.adicionar_creditos()
lucca.detalhar()
isaac = estudande(1,"isaac")
isaac.adicionar_creditos()
isaac.detalhar()