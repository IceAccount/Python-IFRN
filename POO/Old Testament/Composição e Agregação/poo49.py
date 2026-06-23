class Item:
    def __init__(self, produto, quantidade, preço):
        self.produto = produto
        self.quantidade = quantidade
        self.preço = preço
class Pedido:
    def __init__(self,nome):
        self.nome = nome
        self.pedidos = []
    def adicionar_item(self, Item):
        self.pedidos.append(Item)
    def calcular_total(self):
        produtos =  0
        preco_total = 0
        for produto in self.pedidos:
            produtos += produto.quantidade
            preco_total += produto.preço
        print(f"a Compra de {produtos} produtos custou {preco_total:.2f}")

i1 = Item("Manteiga", 320, 30)
i2 = Item("Detergente", 2, 7)

p1 = Pedido("Pedido de Darlan")
p1.adicionar_item(i1)
p1.adicionar_item(i2)
p1.calcular_total()