lista = []

def Depreciar(nomeEquipamento):
    global retornoTexto
    for indice in range(0, len(lista)):
        if nomeEquipamento == lista[indice][0]:
            valorAntigo = lista[indice][1]
            valorAtual = lista[indice][1] * 0.9
            lista[indice][1] = valorAtual
            retornoTexto = f"Valor antigo: {valorAntigo}, o novo valor é: {valorAtual}"
            break
        else:
            retornoTexto = "Não foi identificado este equipamento em nossa base de dados!"
    return retornoTexto

def RemoverEquipamento(numSerial):
    global retorno
    for indice in range(0, len(lista)):
        if numSerial == lista[indice][2]:
            del lista[indice]
            retorno = "Equipamento removido com sucesso!"
            break
        else:
            retorno = "Equipamento não foi localizado em nossa base de dados!"
    return retorno

def AdicionarEquipamento(nome, valor, serial, depart):
    equipamento = [nome, valor, serial, depart]
    lista.append(equipamento)
    return

def ListarEquipamentos():
    for indice in range(0, len(lista)):
        print("")
        print("Equipamento..: ", (indice+1))
        print("Nome.........: ", lista[indice][0])
        print("Valor........: ", lista[indice][1])
        print("Serial.......: ", lista[indice][2])
        print("Departamento.: ", lista[indice][3])
        print("")
    return
