'''
Questão 1
'''

def func(funcao):
    return funcao()

def func2():
    texto = 'Exercicio Função!'
    print(texto)

func(func2)

'''
Questão 2
'''

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando = mestre(fala_oi, 'Antonio')
executando2 = mestre(saudacao, 'Antonio', 'Bem vindo ao Python!')
print(executando)
print(executando2)