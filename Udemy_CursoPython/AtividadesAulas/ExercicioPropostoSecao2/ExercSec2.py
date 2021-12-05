
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número interio.
"""

usuario = input("Digite um número: ")
if usuario.isnumeric():
    result = int(usuario) % 2 == 0
    if result:
        print(f"O número {usuario} é Par!")
    else:
        print(f"O número {usuario} é ímpar!")
else:
    print("Não foi informado um número inteiro!")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input("Por favor, informe a hora: ")
hora = hora[:2]
# print(hora)

if hora.isnumeric():
    hora = int(hora)
    if hora >= 0 and hora <= 11:
        print("Bom dia")
    elif hora <= 17:
        print("Boa Tarde!")
    elif hora < 24:
        print("Boa Noite!")
    else:
        print("Informe um horário valido das 0h às 23h")
else:
    print("Por favor informe a hora em número...")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input("Por favor digite o seu primeiro nome: ")
espaco = int(nome.find(' '))
if espaco != -1:
    nome = nome[:espaco]

tamanho = len(nome)
if tamanho != 0:
    if tamanho < 5:
        print("Seu nome é curto")
    elif tamanho <= 6:
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande")
else:
    print("Por favor informe um nome!")
