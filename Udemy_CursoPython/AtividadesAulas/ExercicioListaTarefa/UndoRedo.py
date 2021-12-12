import os

global resultado, menu

resultado = None
menu = ''

lista_tarefa = []
stg_lista = {
    'adicionar': '',
    'remover': '',
    'acao': ''
}

def menuSistema():
    print()
    print("{:#^50}".format(" Informe a ação desejada "))
    print("{:-^50}".format(" Para adicionar uma tarefa digite A "))
    print("{:-^50}".format(" Para listar uma tarefa digite L "))
    print("{:-^50}".format(" Para Excluir uma tarefa digite E "))
    print("{:-^50}".format(" Para Desfazer a última tarefa D "))
    print("{:-^50}".format(" Para Refazer a última tarefa R "))
    print("{:-^50}".format(" Para Sair digite S "))
    print()


def adicionarTarefa(tarefa):
    item = tarefa.title().strip()
    lista_tarefa.append(item)
    stg_lista['adicionar'] = item
    stg_lista['acao'] = 'adicionar'
    return True


def listarTarefa():
    print()
    print("{:#^50}".format(" LISTA "))
    for indice, item in enumerate(lista_tarefa):
        indice = indice + 1
        print(f'Tarefa {indice} é {item}')
    print("{:#^50}".format(""))
    print()


def removerTarefa(tarefa):
    item = tarefa - 1
    stg_lista['remover'] = lista_tarefa[item]
    stg_lista['acao'] = 'remover'
    lista_tarefa.pop(item)
    return True


def fazerAcao():
    acao = stg_lista['acao']
    if acao == 'adicionar':
        posicao = (lista_tarefa.index(stg_lista['adicionar'])+1)
        removerTarefa(posicao)
        return True
    elif acao == 'remover':
        item = stg_lista['remover']
        adicionarTarefa(item)
        return True
    else:
        return False


while True:
    if menu != 'L':
        os.system('cls' if os.name == 'nt' else 'clean')
    menuSistema()
    if resultado is not None:
        print("{:#^50}".format(" RESULTADO "))
        print(resultado)
        print()
        resultado = None

    menu = input("Digite a ação desejada: ").upper().strip()
    while menu != 'A' and menu != 'L' and menu != 'E' and menu != 'D' and menu != 'R' and menu != 'S':
        os.system('cls' if os.name == 'nt' else 'clean')
        print("{:-^50}".format(" AÇÃO INVALIDA "))
        menuSistema()
        menu = input("Digite a ação desejada: ").upper().strip()

    if menu == 'A':
        tarefa = input("Qual tarefa deseja adicionar a lista? ")
        try:
            adicionarTarefa(tarefa)
            resultado = "Tarefa adicionada com sucesso!"
        except:
            resultado = "Erro inesperado, não foi possível adicionar tarefa!"
            continue
    elif menu == 'L':
        listarTarefa()
    elif menu == 'E':
        listarTarefa()
        tarefa = input("Informe o número de ordem da tarefa a remover: ")
        try:
            tarefa = int(tarefa)
            removerTarefa(tarefa)
            resultado = "Tarefa removida com sucesso!"
        except:
            resultado = "Erro inesperado, não foi possível remover tarefa!"
            continue
    elif menu == 'D':
        try:
            fazerAcao()
        except:
            resultado = "Não há ação para desfazer!"
            continue
    elif menu == 'R':
        try:
            fazerAcao()
        except:
            resultado = "Não há ação para desfazer!"
            continue
    elif menu == 'S':
        break