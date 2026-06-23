class Veiculo:
     def mover(self): 
        return "*movendo*"
class Moto(Veiculo):
     def mover(self): 
        return "rammm rammmmmmmmmmmmmmmmmm"
class Carro(Veiculo):
     def mover(self): 
        return "vrumm"
class Bicicleta(Veiculo):
     def mover(self): 
        return "pam pam"

veiculos = [Veiculo(),Moto(),Carro(),Bicicleta()]
for veiculo in veiculos:
    print(f"{veiculo.__class__.__name__}: {veiculo.mover()}")