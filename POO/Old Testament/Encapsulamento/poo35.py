class Produto:
    def __init__(self, nome, preco, quantidade_em_estoque):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_em_estoque = quantidade_em_estoque
       
    def vender(self, quantidade_em_estoque):
        if quantidade_em_estoque > self.__quantidade_em_estoque:
            print("estoque insuficiente");
            return
        self.__quantidade_em_estoque -= quantidade_em_estoque
       
    def repor_estoque(self, quantidade_em_estoque):
        if quantidade_em_estoque <= 0 :
            print("coloque um numero valido")
            return
        self.__quantidade_em_estoque += quantidade_em_estoque
       
    @property

    def nome(self):
        return self.__nome
    @property
    def preco(self):
        return self.__preco
    @property
    def quantidade_em_estoque(self):
        return self.__quantidade_em_estoque


    @quantidade_em_estoque.setter
    def quantidade_em_estoque(self, value):
        if value < 0:
            return
        self.__quantidade_em_estoque = value
   
    @preco.setter
    def preco(self, value):
        if value < 0:
            return
        self.__preco = value
   
meu_produto = Produto("Iphoe12", 3500.00, 10)


print("\n\n\n")


print(f"Produto: {meu_produto.nome}, Preço: R${meu_produto.preco:.2f}, Estoque: {meu_produto.quantidade_em_estoque}")


meu_produto.vender(3)




meu_produto.repor_estoque(5)




print(f"Estoque atual: {meu_produto.quantidade_em_estoque}")




meu_produto.vender(15) # Tentativa de vender mais do que há em estoque
