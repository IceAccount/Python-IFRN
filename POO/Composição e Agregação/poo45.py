from dataclasses import dataclass

@dataclass
class Professor:
    nome: str
    titulacao: str
    def informaçoes(self):
        print(self.nome, self.titulacao)
@dataclass
class Disciplina:
    nome: str
    professor: Professor
    def informacoes(self):
        print(f"O prof da disciplina é {self.professor.nome} e a materia é {self.nome}")

professor1 = Professor("Murilo", "Espaçonave Jefferson")

disciplina1 = Disciplina("Voação", professor1)

professor1.informaçoes()
disciplina1.informacoes()