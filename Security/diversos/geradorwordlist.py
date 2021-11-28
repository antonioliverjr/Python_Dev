import itertools

string = input("String a ser permutada: ")

resultado = itertools.permutations(string, len(string))
count = 0

for i in resultado:
    print(''.join(i))
    count += 1

print(count)
