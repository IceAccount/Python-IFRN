# @cikey fd9a243ad4a8b28900905b2856e18403
# @sid 20251174010022
# @aid V6.5

import random

n = random.randint(1,100)
p = 0 
while(p != n):
    p = int(input())
    if (p > n):
        print("digite um numero menor")
    elif (p < n):
        print ("digite um numero maior")
    else:
        print (f"parabens! o numero era {p}")