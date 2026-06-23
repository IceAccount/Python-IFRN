class Animal:
    def __init__(self):
        self.grupo = 'Grupo'
    def fazersom(self):
        return "som"



class Cachorro(Animal):
    def __init__(self):
        super().__init__()
        self.grupo = 'Manifero'
    def fazersom(self):
        return "Au au"
