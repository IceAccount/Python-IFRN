class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.__saldo = 0
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente")
    
    def get_saldo(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor invalido")

pessoa = ContaBancaria("Rodrigo")
pessoa.get_saldo(10)
pessoa.get_saldo(-1)
pessoa.get_saldo(0)
pessoa.set_saldo(100)
pessoa.set_saldo(10)

print("valor possuido: ", pessoa.get_saldo)