# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

valor1 = int(input("Digite um numero: "))
valor2 = int(input("Digite outro numero: "))
print("Qual operação deseja (+)(-)(x)(/)")

operador = input("Informe: ")
while operador != "+" and operador != "-" and operador != "x" and operador != "/":
    print("Operador invalido")
    operador = input("Informe: ")
    
operador.lower()

def somar(x, y): return x + y    
    
def subtrair(x, y): return x - y
    
def multiplica(x, y): return x * y 
    
def dividir(x, y): return x / y
    
if operador == "+":
    result = somar(valor1, valor2)
elif operador == "-":
    result = subtrair(valor1, valor2)
elif operador == "x":
    result = multiplica(valor1, valor2)
elif operador == "/":
    if valor2 == 0:
        erro = "Divisão por zero, erro!"
    else:
        result = dividir(valor1, valor2)
else:
    erro = "Erro não esperado!"       

if erro == "":
    print("O resultado da operação %s %s %s é igual à %s" %(valor1, operador, valor2, result))
else:
    print(erro)