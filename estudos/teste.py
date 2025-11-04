nomearchive = "../Python-IFRN/estudos/empresas"
f = open(nomearchive, mode="a+")
print(f.readlines())

#for t in f.readlines():
#    print(t, end="")

f.write("Escrever no arquivo")
f.write("mais uma linha")