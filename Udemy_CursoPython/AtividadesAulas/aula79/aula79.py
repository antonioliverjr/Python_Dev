from itertools import groupby, tee

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'C'},
    {'nome': 'Anderson', 'nota': 'B'},
]


# def ordena(item):
#   return item['nota']

ordena = lambda item: item['nota']


alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

'''
# Sem tee (com list)
for agrupamento, valores_agrupados in alunos_agrupados:
  valores = list(valores_agrupados)
  print(f'Agrupamento: {agrupamento}')
  for aluno in valores:
    print(f'\t{aluno}')
  quantidade = len(valores)
  print(f'\t{quantidade} alunos tiraram nota {agrupamento}')
'''

# Com tee
for agrupamento, valores_agrupados in alunos_agrupados:
  v1, v2 = tee(valores_agrupados)

  print(f'Agrupamento: {agrupamento}')

  for aluno in v1:
    print(f'\t{aluno}')

  quantidade = len(list(v2))
  print(f'\t{quantidade} alunos tiraram nota {agrupamento}')