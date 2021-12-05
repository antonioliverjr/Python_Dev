"""
CPF = ***.***.***-**
"""
print('{:#^50}'.format(''))
print('{:#^50}'.format(' VÁLIDADOR DE CPF '))
print('{:#^50}'.format(''))
while True:
    cpf = input("Informe o CPF para validação: ")
    if len(cpf) != 11:
        continue
    else:
        break

cpf = cpf.replace('.', '').replace('-', '').replace(',', '')
valida_cpf = cpf[0:9]
print('{:#^50}'.format(''))
###################################################
soma_cpf = 0
for indice, mult in enumerate(range(10, 1, -1)):
    soma_cpf += int(valida_cpf[indice]) * mult

formula1 = 11 - (soma_cpf % 11)
digito1 = '0' if (formula1 > 9) else str(formula1)

valida_cpf += digito1
###################################################
soma_cpf = 0
for indice, mult in enumerate(range(11, 1, -1)):
    soma_cpf += int(valida_cpf[indice]) * mult

formula2 = 11 - (soma_cpf % 11)
digito2 = '0' if (formula2 > 9) else str(formula2)

valida_cpf += digito2
##################################################
print('{:#^50}'.format(' CPF Válido ' if cpf == valida_cpf else ' CPF inválido! '))
print('{:#^50}'.format(''))