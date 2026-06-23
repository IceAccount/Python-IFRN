class Forma:
    def __init__(self,base,altura):
        self.altura = base
        self.base = altura
    def area(self):
        areat = self.base*self.altura
        print(f"a base do retangulo é {areat}.")
    
class Retangulo(Forma):
    def __init__(self, base, altura):
        super().__init__(base, altura)


r1 = Retangulo(10, 50)
r1.area()