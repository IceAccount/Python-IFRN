# @cikey fd9a243ad4a8b28900905b2856e18403
# @sid 20251174010022
# @aid V7.3

import random

numeros_sorteados = random.sample(range(1, 40), 25)
numeros_sorteados.sort()
print(numeros_sorteados)