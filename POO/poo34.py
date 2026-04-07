class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
       
    def despositar(self, value):
        if value <= 0:
            return
        self.__saldo += value


    def sacar(self, value):
        if self.__saldo < value:
            self.__saldo = 0
            return
        self.__saldo -= value
       
    def consultar_dados(self):
        print(self.__saldo)
       
    def get_saldo(self):
        return self.__saldo
    def set_saldo(self, value):
        self.__saldo = value
   
       
oiw = ContaBancaria("Carlos", 70)
oiw.consultar_dados()
oiw.despositar(67)
oiw.consultar_dados()
oiw.sacar(51)


oiw.consultar_dados()