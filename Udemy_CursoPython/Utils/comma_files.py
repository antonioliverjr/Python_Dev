import csv


with open('clientes.csv', 'r') as file:
    # lista = csv.reader(file)
    # next(lista)

    # for valor in lista:
    #     print(valor)
    # dados = csv.DictReader(file)
    #
    # for dado in dados:
    #     print(dado['Nome'], dado['Sobrenome'], dado['E-mail'], dado['Telefone'])

    dados = [x for x in csv.DictReader(file)]

with open('clientes2.csv', 'w') as file:
    escreve = csv.writer(
        file,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    chaves = dados[0].keys()
    chaves = list(chaves)
    escreve.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3],
        ]
    )

    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )
