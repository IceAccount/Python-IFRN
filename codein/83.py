# @cikey fd9a243ad4a8b28900905b2856e18403
# @sid 20251174010022
# @aid V8.3

with open("aaa.txt","r",encoding="utf-8") as arquivo_original:
    conteudo = arquivo_original.read()
with open("bbb.txt","w",encoding="utf-8") as copiar:
     copiar.write(conteudo)  
print("copiado com sucesso")