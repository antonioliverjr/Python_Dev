string = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'

'''
Separar em grupos de 0 à 9 em uma lista
'''
tam = 10
contadores = [i for i in range(0, len(string), tam)]
tuplas = [(i, i+tam) for i in range(0, len(string), tam)]
lista = [string[i: i+tam] for i in range(0, len(string), tam)]

print(contadores)
print(tuplas)
print(lista)

retorno = '.'.join(lista)
print(retorno)

print(retorno.replace('.', ','))

