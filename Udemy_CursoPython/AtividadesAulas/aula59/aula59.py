def funcao(arg, arg2):
    return arg * arg2

var = funcao(2, 2)
print(var)

#Função lambda, reduzindo código
a = lambda x, y: x * y
print(a(2, 2))

lista = [
    ['Produto1', 13],
    ['Produto2', 6],
    ['Produto3', 7],
    ['Produto4', 50],
    ['Produto5', 8],
]
print(sorted(lista, key=lambda item: item[1]))
print(lista)
lista.sort(key=lambda item: item[1], reverse=True)
print(lista)
