from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

print(escritor.nome)
print(caneta.marca)
maquina.escrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()
