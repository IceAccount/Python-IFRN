class Aluno:
    def __init__(self, nome):
        self.nome = nome

class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []
    def adicionar_aluno(self, Aluno):
        self.alunos.append(Aluno)
    def lista_de_alunos(self):
        for Aluno in self.alunos:
            print(Aluno.nome)

class Escola:
    def __init__(self,nome):
        self.nome = nome
        self.turmas = []
    def adicionar_turma(self, Turma):
        self.turmas.append(Turma)
    def lista_de_turmas(self):
        for Turma in self.turmas:
            print(Turma.nome)


a1 = Aluno("Isaac")
a2 = Aluno("Miguel")
a3 = Aluno("Joao Pedro")

t1 = Turma("9 ano A")
t2 = Turma("9 ano B")

t1.adicionar_aluno(a1)
t1.adicionar_aluno(a3)
t2.adicionar_aluno(a2)

e1 = Escola("Barão de Ceará-Mirim")
e1.adicionar_turma(t1)
e1.adicionar_turma(t2)

e1.lista_de_turmas()
t1.lista_de_alunos()
t2.lista_de_alunos()