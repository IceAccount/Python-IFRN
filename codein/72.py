# @cikey fd9a243ad4a8b28900905b2856e18403
# @sid 20251174010022
# @aid V7.2


#begin_inputs
palavra = "revenant"
letras = []
#end_inputs 
chances = 4

ganhou = False

while True:

    for letra in palavra:

        if letra.lower() in letras:
            print(letra, end=" ")
        else:
            print("_", end=" ")

    print(f"Você tem {chances} chances")
    tentativa = input("Escolha uma letra para adivinhar: ")

    letras.append(tentativa.lower())

    if tentativa.lower() not in palavra.lower():

        chances -= 1

    ganhou = True

    for letra in palavra:

        if letra.lower() not in letras:

            ganhou = False

    if chances == 0 or ganhou:

        break

if ganhou:
    print(f"ganhou, the palavra era {palavra}")
else:
    print(f"perdeukkkkkkkkkk era {palavra}")
    