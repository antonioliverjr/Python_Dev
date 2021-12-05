"""
CPF = ***.***.***-**
"""
import random

print('{:#^50}'.format(''))
print('{:#^50}'.format(' GERADOR DE CPF '))
print('{:#^50}'.format(''))

cpf = str(random.randint(100000000, 999999999))
###################################################
soma_cpf = 0
for indice, mult in enumerate(range(10, 1, -1)):
    soma_cpf += int(cpf[indice]) * mult

formula1 = 11 - (soma_cpf % 11)
digito1 = '0' if (formula1 > 9) else str(formula1)

cpf += digito1
###################################################
soma_cpf = 0
for indice, mult in enumerate(range(11, 1, -1)):
    soma_cpf += int(cpf[indice]) * mult

formula2 = 11 - (soma_cpf % 11)
digito2 = '0' if (formula2 > 9) else str(formula2)

cpf += digito2
##################################################
print('{:#^50}'.format(' CPF Válido {}.{}.{}-{} '.format(cpf[0:3], cpf[3:6], cpf[6:9], cpf[9:11])))
print('{:#^50}'.format(''))