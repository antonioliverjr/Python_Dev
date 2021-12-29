import json


clientes_dicionario = {
    1: {
        'nome': 'Antonio Junior',
        'sobrenome': 'Oliveira',
        'idade': 35,
        'altura': 1.90,
        'peso': 113.0
    },
    2: {
            'nome': 'Maria',
            'sobrenome': 'Oliveira',
            'idade': 55,
            'altura': 1.67,
            'peso': 63.0
        },
    3: {
            'nome': 'Pedro',
            'sobrenome': 'Faria',
            'idade': 32,
            'altura': 1.85,
            'peso': 79.5
        }
}

lista = [x for x in range(1, 10)]
dados_json = json.dumps(lista)
print(lista)
print(dados_json)

clientes = json.dumps(clientes_dicionario, indent=4)
print(clientes)

dicionario = json.loads(clientes)
for k, v in dicionario.items():
    print(k, v)

with open('clientes.json', 'w') as file:
    json.dump(clientes_dicionario, file, indent=4)

with open('clientes.json', 'r') as file:
    dados = json.load(file)

for k, v in dados.items():
    print(k, v)

