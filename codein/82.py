# @cikey fd9a243ad4a8b28900905b2856e18403
# @sid 20251174010022
# @aid V8.2

with open("aaa.txt","w+",encoding="utf-8") as linha:
    linha.write("Linha 1\n")
    linha.write("Linha 2\n")
    linha.write("Linha 3\n")
    linha.write("Linha 4\n")
    linha.write("Linha 5")
with open("aaa.txt","r",encoding="utf-8") as linha:  
    linhas = linha.readlines()
print(f"linhas = {len(linhas)}")