# @cikey fd9a243ad4a8b28900905b2856e18403
# @sid 20251174010022
# @aid V4.2


#begin_inputs
#mantenha esse trecho. o input será manipulado aqui.
#end_inputs

maior = 0

for i in range(10):
    idade = input()
    if idade >= 18:
        maior += 1

print(maior)
