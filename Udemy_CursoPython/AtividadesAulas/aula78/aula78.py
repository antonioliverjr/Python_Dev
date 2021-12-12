from itertools import combinations, permutations, product

pessoas = ['Luiz', 'Andre', 'Eduardo', 'Leticia', 'Antonio', 'Cassia']

for grupo in combinations(pessoas, 3):
    print(grupo)

print()

for grupos in permutations(pessoas, 2):
    print(grupos)

print()

for grupos2 in product(pessoas, repeat=2):
    print(grupos2)