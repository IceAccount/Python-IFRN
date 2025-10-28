# @cikey fd9a243ad4a8b28900905b2856e18403
# @sid 20251174010022
# @aid V6.4

# Jogo de Craps

#begin_inputs
#end_inputs
dados_primeira = int(input(""))
if dados_primeira in (7, 11):
    print("Voce ganhou!")
elif dados_primeira in (2, 3, 12):
    print("Voce perdeu!")
else:
    ponto = dados_primeira
    while True:
        try:
            jogada = int(input(""))
        except:
            break

        if jogada == ponto:
            print("Voce ganhou!")
            break
        elif jogada == 7:
            print("Voce perdeu!")
            break
