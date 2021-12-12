from dados import produtos, pessoas, lista
from functools import reduce

acumula = 0
for item in lista:
    acumula += item
print(acumula)

soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)

soma_idade = reduce(lambda ac, i: i['idade'] + ac, pessoas, 0)
print(round(soma_idade/len(pessoas)))
