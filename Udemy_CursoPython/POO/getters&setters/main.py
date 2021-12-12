from produto import Produto

p1 = Produto('Camiseta', 50)
p1.desconto(10)
print(p1)
print(p1.preco)

p2 = Produto('Caneca', 'R$15')
p2.desconto(10)
print(p2.preco)
print(p2)
