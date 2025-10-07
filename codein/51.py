# @cikey fd9a243ad4a8b28900905b2856e18403
# @sid 20251174010022
# @aid V5.1


#begin_inputs

#end_inputs
peso_total = 0
while True:
    p = input()
    if peso_total + p >= 500:
        print('Peso excedido')
        break
    peso_total += p