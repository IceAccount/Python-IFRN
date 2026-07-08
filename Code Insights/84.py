# @cikey fd9a243ad4a8b28900905b2856e18403
# @sid 20251174010022
# @aid V8.4

Dados = {}
with open("ccc.txt","w",encoding="utf-8") as dados:
   for n in range(5):
     Nome = input("Escreva seu Nome:")
     Cpf =  input("Escreva seu CPF:")
     Dados[Nome] = Cpf
     dados.write(f"{Nome};{Cpf}\n")
print("_______________________")
with open("ccc.txt","r",encoding="utf-8") as leia:
    ler = leia.read()
    print(ler.strip())