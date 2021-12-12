carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))
print(carrinho)

total = 0
for produto in carrinho:
    total += produto[1]
print(total)

total_lista = sum([float(y) for z, y in carrinho])
print(total_lista)