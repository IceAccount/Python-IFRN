class ContaCorrente:
    def __init__(self, nome, cpf, saldo):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo
    def depositar(self):
        self.depositar = int(input("depositar:"))
        self.saldoatual = self.saldo + self.depositar
        print (self.saldoatual)
    def sacar(self):
        self.sacar = int(input("sacar:"))
        self.saldoatual2 = self.saldoatual - self.sacar
        print (self.saldoatual)
    def mostrar_dados(self):
        print(self.nome)
        print(self.cpf)
        print(self.saldoatual)

Leticia = ContaCorrente("Leticia", 1232452465, 10)
Leticia.depositar()
Leticia.sacar()
Leticia.mostrar_dados()