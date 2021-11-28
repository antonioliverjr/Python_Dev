def ProcuraResposta(palavra):
    if "SIM" in palavra:
        palavra = "SIM"
    elif "NAO" in palavra or "NÃO" in palavra:
        palavra = "NAO"
    return palavra

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = ProcuraResposta(input("Suspeita de doença infectocontagiosa? ").upper())
valor = 1

while (doenca_infectocontagiosa != "SIM") and (doenca_infectocontagiosa != "NÃO")\
        and (doenca_infectocontagiosa != "NAO"):
    print("Informe se há, suspeita de doença infectocontagiosa? ")
    doenca_infectocontagiosa = ProcuraResposta(input("Sim ou Não? ").upper())
    valor += 1
    if valor == 3:
        break

if (doenca_infectocontagiosa != "SIM") and (doenca_infectocontagiosa != "NÃO")\
            and (doenca_infectocontagiosa != "NAO"):
    print("Esgotado a quantidade de vezes para informar se há suspeita de doença infectocontagiosa, inicie novamente!")
else:
    if idade >= 65:
        if doenca_infectocontagiosa == "SIM":
            print("O paciente " + nome + " POSSUI atendimento prioritário e deve ser direcionado para sala reservada!")
        else:
            print("O paciente " + nome + " POSSUI atendimento prioritário!")
    elif doenca_infectocontagiosa == "SIM":
        print("O paciente ", nome, " deve ser direcionado para sala de espera reservada!")
    else:
        print(f"O paciente {nome} NÃO possui atendimento prioritário! E pode aguardar na sala comum!")