# @cikey fd9a243ad4a8b28900905b2856e18403
# @sid 20251174010022
# @aid V5.1


#begin_inputs
pesos = (45, 88, 67, 102, 80, 95, 66) 
#end_inputs
limite = 500
elevator = 0
pesomax = sum(pesos) + elevator
if pesomax > limite:
    print("peso excedido")
#o codigo ta com o resultado certo mas a formatacao nao devia ta assim.
#e eu nao sei como que devia ser