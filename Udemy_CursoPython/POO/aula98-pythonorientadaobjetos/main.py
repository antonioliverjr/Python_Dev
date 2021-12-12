from pessoa import Pessoa

p1 = Pessoa('Antonio', 35)
p2 = Pessoa('Cassia', 29)

p1.falar('Programação Orientada a Objetos')
p2.falar('Nada')

p1.comer('Jaca')
p1.paraComer()
p1.paraComer()
p1.comer('Jaca')
p1.comer('Jaca')

print(p1.get_ano_nascimento())

p3 = Pessoa.por_ano_nascimento('Ana Cecilia', 2012)
print(p3)

print(Pessoa.gera_id())

# p1.nome = 'Luiz'
# p2.nome = 'João'
# print(p1.nome)
