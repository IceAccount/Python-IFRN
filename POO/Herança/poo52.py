class Animal:
    def __init__(self):
        self.grupo = 'Grupo'




class Cachorro(Animal):
    def __init__(self):
        super().__init__()
        self.grupo = 'Manifero'


Tobinho = Cachorro()
