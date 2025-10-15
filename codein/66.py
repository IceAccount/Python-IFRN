# @cikey fd9a243ad4a8b28900905b2856e18403
# @sid 20251174010022
# @aid V6.6

import random
numero_min = 1
numero_max = 1000000
numero_secreto = random.randint(numero_min, numero_max)
LIMITE_DE_TENTATIVAS = 50
tentativas = 1
tentativa = int(input("Fale um numero entre 1 e 1 milhão: "))

while tentativa != numero_secreto: 
    if tentativa > numero_secreto:
        print("O numero que voce escolheu é MAIOR que o numero secreto, tente de novo")
    elif tentativa < numero_secreto:
        print("O numero que voce escolheu é MENOR que o numero secreto, tente de novo")

    print(f"Você ainda tem {LIMITE_DE_TENTATIVAS} tentativas restantes")  
    LIMITE_DE_TENTATIVAS -= 1
    tentativa = int(input("Fale um numero entre 1 e 100: "))
    tentativas += 1

    if tentativas > LIMITE_DE_TENTATIVAS:
         print("Você execeu o número máximo de tentativas, você perdeu.")
         exit()
print(f"Voce acertou o numero era {numero_secreto} e você conseguiu em {tentativas} tentativas")



