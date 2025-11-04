nomearchive = "../Python-IFRN/estudos/Phasmophobia"
f = open(nomearchive, mode="r")
phasmophobia = (f.readlines())
f.close

for l in f.readlines():
    print(l)

phasmophobia[6] = "revenant\n"
phasmophobia[7] = "mare\n"
phasmophobia[8] = "goryo\n"
phasmophobia[9] = "onryo\n"

f = open(nomearchive, mode="w")
for l in phasmophobia():
    f.write(l)
f.close()
#    print(t, end="")

# f.write("Escrever no arquivo")
# f.write(" mais uma linha")
# f.close()