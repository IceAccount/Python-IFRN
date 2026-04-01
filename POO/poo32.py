class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.__saldo = 0
    def depositar(self):
        while True:
            saldodepositado = int(input("Quanto deseja depositar? "))
            if saldodepositado == 0:
                print("tente novamente... ")
            else:
                self.__saldo += saldodepositado
                break
    def sacar(self):
        while True:
            saldosacado = int(input("Quanto deseja sacar? "))
            if saldosacado == 0:
                print("Coloque um valor válido. ")
            else:
                self.__saldo -= saldosacado
                break
    def consultar_saldo(self):
        print(self.titular)
        print(self.__saldo)

Pobre1 = ContaBancaria("Leticia")
Pobre1.depositar()
Pobre1.sacar()
Pobre1.consultar_saldo()