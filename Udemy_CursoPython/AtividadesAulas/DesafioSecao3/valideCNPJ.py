from itertools import tee

cnpj = '04.252.011/0001-10'
cnpj2 = '40.688.134/0001-61'
cnpj3 = '71.506.168/0001-11'
cnpj4 = '12.544.992/0001-05'


def removerCaracteres(cnpj):
    cnpj_rem = [x.replace('.', '').replace('/', '').replace('-', '') for x in cnpj]
    cnpj_rem = [int(x) for x in cnpj_rem if x != '']
    return cnpj_rem

def validaCnpj(cnpj):
    cnpj_atual = removerCaracteres(cnpj)
    valores = [int(x) for x in cnpj_atual[0:-2] if x != '']
    validador = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    valor_primeiro, valor_segundo = tee(valores)
    primeiro_digito, segundo_digito = tee(validador)

    lista1 = []
    lt1 = [x for x in valor_primeiro]
    lt2 = [y for y in primeiro_digito]
    total = zip(lt1, lt2[1:])
    for item in total:
        lista1.append((item[0]*item[1]))
    calc1 = 11 - (sum(lista1) % 11)
    digito1 = 0 if calc1 > 9 else calc1

    lista2 = []
    lt3 = [x for x in valor_segundo]
    lt3.append(digito1)
    lt4 = [y for y in segundo_digito]
    total2 = zip(lt3, lt4)
    for item in total2:
        lista2.append((item[0]*item[1]))
    calc2 = 11 - (sum(lista2) % 11)
    digito2 = 0 if calc2 > 9 else calc2

    lt3.append(digito2)
    cnpj_atual = ''.join(str(x) for x in cnpj_atual)
    cnpj_verificado = ''.join(str(x) for x in lt3)

    if cnpj_atual == cnpj_verificado:
        return True
    else:
        return False

if __name__ == '__main__':
    if validaCnpj(input("Informe um CNPJ para verificação: ")):
        print("CNPJ é válido!")
    else:
        print("CNPJ Inválido!")
