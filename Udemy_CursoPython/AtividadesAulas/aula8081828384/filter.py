from dados import produtos, pessoas, lista

nova_lista = filter(lambda item: item > 5, lista)
# nova_lista = [x for x in lista if x > 5]
print(list(nova_lista))
print()

novos_produtos = filter(lambda x: x['preco'] > 50, produtos)
for produto in novos_produtos:
    print(produto)
print()



