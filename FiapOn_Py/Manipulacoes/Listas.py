from Manipulacoes.equipamentos import *
import os

resposta = "SIM"

def ProcuraSim(palavra):
    if "SIM" in palavra or "S" in palavra:
        palavra = "SIM"
    return palavra

while resposta == "SIM":
    print("")
    print("Escolha uma opção:")
    print("Para adicionar equipamento, digite 1")
    print("Para remover equipamento, digite 2")
    print("Para depreciar equipamento, digite 3")
    print("Para listar equipamentos, digite 4")
    menu = int(input("Informe a opção: "))
    print("")

    while menu != 1 and menu != 2 and menu != 3 and menu != 4 and menu == '':
        print("Por favor digite uma opção valida!")
        menu = int(input("Informe a opção: "))

    if menu == 1:
        nomeEquipamento = input("Equipamento: ")
        valorEquipamento = float(input("Valor: "))
        serialEquipamento = int(input("Número Serial: "))
        departamentoEquipamento = input("Departamento: ")
        AdicionarEquipamento(nomeEquipamento, valorEquipamento, serialEquipamento, departamentoEquipamento)
        print("Equipamento adicionado com sucesso!")
    elif menu == 2:
        numeroSerial = int(input("Digite o serial do equipamento que deseja excluir: "))
        resultado = RemoverEquipamento(numeroSerial)
        print(resultado)
    elif menu == 3:
        nome = input("Digite o nome do equipamento a depreciar 10%: ")
        resultado = Depreciar(nome)
        print(resultado)
    else:
        ListarEquipamentos()

    print("")
    resposta = ProcuraSim(input("Digite SIM para continuar: ").upper())
    os.system('clear')
