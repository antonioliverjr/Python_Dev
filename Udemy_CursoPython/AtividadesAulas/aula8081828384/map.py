from dados import produtos, pessoas, lista

print(lista)
nova_lista = list(map(lambda x: x*2, lista))
# nova_lista = [x * 2 for x in lista]
print(nova_lista)
print()

def aumenta_preco(p):
    p['preco_novo'] = round(p['preco'] * 1.05, 2)
    return p

produtos = map(aumenta_preco, produtos)

for produto in produtos:
    print(produto)
print()

nomes = map(lambda p: p['nome'], pessoas)
for pessoa in nomes:
    print(pessoa)

