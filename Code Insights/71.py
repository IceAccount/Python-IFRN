# @cikey fd9a243ad4a8b28900905b2856e18403
# @sid 20251174010022
# @aid V7.1


#begin_inputs
letras = input('')
#end_inputs
import string
alfabeto = ['a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letras_disponveis = []
tem_letras = False
for letra in alfabeto:
    if letra not in letras:
        letras_disponveis.append(letra)
        tem_letras = True
if tem_letras:
    print(letras_disponveis)
else:
    print('[]')


