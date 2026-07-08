# @cikey fd9a243ad4a8b28900905b2856e18403
# @sid 20251174010022
# @aid V6.2


#begin_inputs
n = int(input(""))
#end_inputs
def trianguloretangulo(n):
    for i in range(1, n + 1):
        for r in range(1, i + 1):
            print(r, end=' ')
        print()
trianguloretangulo(n)