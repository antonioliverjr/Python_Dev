
def func(a1, a2, a3, a4, a5,nome=None, a6=None):
    return a1, a2, a3, a4, a5, nome, a6

print(func(1,2,3,4,5))

def func2(*args, **kwargs):
    print(args, kwargs)
    nome = kwargs.get('nome')
    print(nome)

func2(1, 2, 3, nome='Junior')


'''
Aula 57
'''
variavel = 'valor'

def func():
    global total
    total = 10
    print(variavel)

func()
print(total)