from classes import *

"""
Associação - Usa | Agregação - Tem | Composição - É dono | A Herança - É
"""

c1 = Cliente('Antonio', 35)
print(c1.nome)
c1.falar()
c1.comprar()
print()

a1 = Aluno('Maria', 40)
print(a1.nome)
a1.falar()
a1.estudar()
print()

c2 = ClienteVIP('Cassia', 29, 'Santos')
print(c2.nome)
c2.falar()
c2.comprar()
