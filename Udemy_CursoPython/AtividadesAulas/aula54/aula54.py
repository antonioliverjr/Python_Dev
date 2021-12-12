def bemVindo(saudacao, nome):
    print('Olá '+nome+' '+saudacao)

bemVindo('Estamos treinando Python', 'Antonio')

def somaTres(x, y, z):
    print(x+y+z)

somaTres(10, 15, 20)

def aumentoValor(num, per):
    return num * (1+(per/100))

valor = aumentoValor(35, 100)
print(valor)

def divisivel(valor):
    if valor % 5 == 0 and valor % 3 == 0:
        return 'Fizz Buzz'
    if valor % 3 == 0:
        return 'Fizz'
    if valor % 5 == 0:
        return 'Buzz'
    return valor

print(divisivel(30))