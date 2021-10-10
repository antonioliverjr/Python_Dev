import sys
#Definindo as variantes da calculadora
try:
    def soma(a, b):
        return a + b
    def menos(a, b):
        return a - b
    def vezes(a, b):
        return a * b
    def divid(a, b):
        return a / b
#Inserindo um valor para calculo da tabuada, com estrutura de verificação até 3 vezes de erro
    opcao = 1
    while opcao == 1:
        contagem = 0
        num = int(input('Digito um valor para calcularmos a tabuada: '))
        while num < 0:
            num = int(input('Digito um valor valido para calcularmos a tabuada: '))
            contagem += 1
            if contagem > 1:
                sys.exit('Estamos encerrando devido a inclusão errada do valor!')
        print('\nEscolha a opção que deseja o calculo:')
#Informar o tipo de calculo desejado, com estrutura de verificação
        tipo = str(input('Para Soma(+), Substração(-), Multiplicação(x), Divisão(/) = '))
        while tipo != '+' and  tipo != '-' and tipo != 'x' and tipo != 'X' and tipo != '/':
            tipo = str(input('Digite corretamente: Soma(+), Substração(-), Multiplicação(x), Divisão(/) = '))
#Calculando os dados informados de 0 a 10!
        for x in range(11):
            if tipo == '/':
                if x == 0:
                    resultado = 0
                elif x > 0:
                    resultado = round(divid(num, x), 2)
            elif tipo == '+':
                resultado = soma(num, x)
            elif tipo == '-':
                resultado = menos(num, x)
            elif tipo == 'x':
                resultado = vezes(num, x)
            elif tipo == 'X':
                resultado = vezes(num, x)
            print('{} {} {} = {}'.format(num, tipo, x, resultado))
#Continuando ou encerrando o código
        print('\nDigite 1 - Para iniciar novamente \nDigite 2 - Para Sair')
        opcao = int(input('\nQual opção deseja? '))
        while opcao != 1 and opcao != 2:
            opcao = int(input('Opção invalida, 1 Iniciar e 2 Sair: '))
    sys.exit('Encerrando a calculadora!')
except ValueError:
    print('Informação inserida incorreta!')