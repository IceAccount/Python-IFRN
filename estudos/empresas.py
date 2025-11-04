nomearchive = "../Python-IFRN/estudos/empresas"
f = open(nomearchive)

for t in f.readlines():
    print(t, end="")

#f.write("Escrever no arquivo")
#f.write("mais uma linha")