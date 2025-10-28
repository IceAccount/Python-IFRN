# @cikey fd9a243ad4a8b28900905b2856e18403
# @sid 20251174010022
# @aid V6.6

import random
numero_min = 1
numero_max = 1000000
numero_secreto = random.randint(numero_min, numero_max)
LIMITE_DE_TENTATIVAS = 50
tentativas = 0


tentativa = int(input("Fale um numero entre 1 e 1 milhao: "))

while tentativa != numero_secreto:

    if tentativa > numero_secreto:
        print("O numero que voce escolheu e MAIOR que o numero secreto, tente de novo")
    else:
        print("O numero que voce escolheu e MENOR que o numero secreto, tente de novo") 

    tentativas += 1
    restante = LIMITE_DE_TENTATIVAS - tentativas

    if tentativas > LIMITE_DE_TENTATIVAS:
         print("Voce execeu o numero máximo de tentativas, você perdeu.")
         exit()

    print(f"Voce ainda tem {restante} tentativas restantes.")

    tentativa = int(input("Fale um numero entre 1 e 1 milhao: "))

if tentativa == numero_secreto:
    print(f"Voce acertou o numero era {numero_secreto} e você conseguiu em {tentativas} tentativas e sobrou {restante} tentativas")
