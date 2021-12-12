lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_soma = [x+y for x, y in zip(lista_a, lista_b)]

print(lista_soma)

from itertools import zip_longest

lista_c = [10, 2, 34, 41, 56, 67, 79]
lista_d = [12, 23, 30, 44]

lista_soma2 = [x+y for x, y in zip_longest(lista_c, lista_c, fillvalue=0)]

print(lista_soma2)
