class Funcionario:
    def __init__(self, nome, sal):
        self.nome = nome
        self.salario = sal
    def exibir_dados(self):
        print(f"Funcionario {self.nome} recebe {self.salario}.")
    
class Gerente(Funcionario):
    def __init__(self, nome, sal, bonus):
        super().__init__(nome, sal)
        self.bonus = bonus
    def exibir_dados(self):
        print(f"Funcionario {self.nome} recebe {self.salario} e o bonus é {self.bonus}")

class Desenvolvedor(Funcionario):
    def __init__(self, nome, sal, linguagem):
        super().__init__(nome, sal)
        self.linguagem = linguagem
    def exibir_dados(self):
        print(f"Funcionario {self.nome} recebe {self.salario} e trabalha com {self.linguagem}")    
    
g1 = Gerente("Car", 4500, 40)

g1.exibir_dados()

d1 = Desenvolvedor("Fabio", 300, "C")
d1.exibir_dados()