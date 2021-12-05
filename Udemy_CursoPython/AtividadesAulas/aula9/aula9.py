texto = 'valor'
lista = [1, 2, 3, 4]

#          0   1        2   3   4
lista2 = ['A','Bacana','C','D','E']
print(lista2[0])
print(lista2[1][0])

string = 'ABCDE'
print(string[2])

lista2[4] = 'Outra Coisa'
print(lista2)

lista.append(5)
lista.extend('6')
lista.insert(3, 7)
lista.pop(0)
print(lista)
del lista[3]
print(lista)
lista.clear()
print(lista)

l1 = []
for i in range(10):
    l1.append(i+1)
print(l1)
del(l1[3:5])
print(l1)
l1.pop()
print(l1)

for i in range(10):
    if len(l1) >= (i+1):
        l1[i] = i+1
    else:
        l1.append(i+1)
print(l1)
