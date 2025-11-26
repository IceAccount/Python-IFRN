# @cikey fd9a243ad4a8b28900905b2856e18403
# @sid 20251174010022
# @aid V8.5
contatos = ["phasmophobia.txt"]

def adicionar_contato():
    nome = input("Fale o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    contatos.append({"nome": nome, "telefone": telefone})
    print(f"Contato {nome} foi adicionado\n")

def ver_contato():
    nome = input("Fale o nome para buscar: ")
    encontrado = False
    for contato in contatos:
        if contato['nome'].lower() == nome.lower():
            print(f"Telefone de {contato['nome']}: {contato['telefone']}\n")
            encontrado = True
            break
    if not encontrado:
        print("Contato não encontrado\n")

while True:
    print("CONTATOS")
    print("1 - Adicionar")
    print("2 - Procurar")
    print("3 - Sair")
    escolha = input("Escolha 1, 2 ou 3: ")

    if escolha == '1':
        adicionar_contato()
    elif escolha == '2':
        ver_contato()
    elif escolha == '3':
        exit()
    else:
        print('Escolha errada, tente de novo\n')




