sequencia1 = 53590
# saída = 90
sequencia2 = 67403098567819
# saída = 5678
sequencia3 = 9012364509789
# saída = 90123


def verificaMaior(lista):
    tam = 0
    retorno = []
    for valor in lista:
        if len(valor) > tam:
            tam = len(valor)
            retorno = [x for x in valor]
    return retorno


def ver_sequencia(lista):

    def adicionarSequencia(atual, proximo):
        if atual in sequencia:
            sequencia.append(proximo)
        else:
            sequencia.append(atual)
            sequencia.append(proximo)

    stg_seq = []
    sequencia = []
    listagem = [x for x in str(lista)]
    for indice, valor in enumerate(listagem):
        if indice < (len(listagem)-1):
            if int(valor)+1 == int(listagem[indice+1]):
                adicionarSequencia(valor, listagem[indice + 1])
            elif int(valor) == 9 and int(listagem[indice+1]) == 0:
                adicionarSequencia(valor, listagem[indice + 1])
            else:
                if len(sequencia) > 0:
                    stg_seq.append([x for x in sequencia])
                    sequencia.clear()
    if len(stg_seq) > 0:
        sequencia = verificaMaior(stg_seq)
    sequencia_result = ''.join([x for x in sequencia])
    return sequencia_result


print(ver_sequencia(sequencia1))
print(ver_sequencia(sequencia2))
print(ver_sequencia(sequencia3))
