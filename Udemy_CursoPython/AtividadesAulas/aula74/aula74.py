from itertools import zip_longest

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']

estados = ['SP', 'MG', 'BA']

cidades_estados = zip(estados, cidades)

cidades_estados2 = zip_longest(estados, cidades, fillvalue='Estado')

# print(list(cidades_estados))
# print(dict(cidades_estados))
for valor in cidades_estados:
    print(valor[0]+'-'+valor[1])

for valor2 in cidades_estados2:
    print(valor2)
