# @cikey fd9a243ad4a8b28900905b2856e18403
# @sid 20251174010022
# @aid V6.4

#begin_inputs
print("Fale um numero entre 2 e 12")
dados_primeira = int(input(""))
#end_inputs
if dados_primeira in (7, 11):
	print("Você Ganhou!")
elif dados_primeira in (2, 3, 12):
    print("Você Perdeu!")
else:
    ponto = dados_primeira
    print(f"Seu ponto é {ponto}")
    
    while True:
        print("Digite a segunda jogada de dados: ")
        nova_jogada = int(input())
        if nova_jogada == ponto:
            print("Você Ganhou!")
            break
        elif nova_jogada == 7:
            print("Você Perdeu!")
            exit()
        else:
            print("Tente novamente")
