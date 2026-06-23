class ContaCorrente:
    def __init__(self, nome, cpf, saldo):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo
    def depositar(self):
        self.depositar = int(input("depositar:"))
        self.saldo = self.saldo + self.depositar
        print (self.saldo)
    def sacar(self):
        self.sacar = int(input("sacar:"))
        self.saldo = self.saldo - self.sacar
        print (self.saldo)
    def mostrar_dados(self):
        print(self.nome)
        print(self.cpf)
        print(self.saldo)

Leticia = ContaCorrente("Leticia", 1232452465, 10)
Leticia.depositar()
Leticia.sacar()
Leticia.mostrar_dados()