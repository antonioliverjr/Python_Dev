import sys
try:
	aluno = str(input('Por favor, digite o nome do aluno: '))
	contagem = 0
	nota1 = int(input('Escreva a nota do 1º trimestre do aluno: '))
	while nota1 > 10 or nota1 < 0:
		nota1 = int(input('Nota invalida! Escreva a nota do 1º trimestre do aluno: '))
		contagem += 1
		if contagem > 1:
			sys.exit('Estamos encerrando devido a inclusão errada de dados!')
	contagem = 0
	nota2 = int(input('Escreva a nota do 2º trimestre do aluno: '))
	while nota2 > 10 or nota2 < 0:
		nota2 = int(input('Nota invalida! Escreva a nota do 2º trimestre do aluno: '))
		contagem += 1
		if contagem > 1:
			sys.exit('Estamos encerrando devido a inclusão errada de dados!')
	contagem = 0
	nota3 = int(input('Escreva a nota do 3º trimestre do aluno: '))
	while nota3 > 10 or nota3 < 0:
		nota3 = int(input('Nota invalida! Escreva a nota do 3º trimestre do aluno: '))
		contagem += 1
		if contagem > 1:
			sys.exit('Estamos encerrando devido a inclusão errada de dados!')
	contagem = 0
	nota4 = int(input('Escreva a nota do 4º trimestre do aluno: '))
	while nota4 > 10 or nota4 < 0:
		nota4 = int(input('Nota invalida! Escreva a nota do 4º trimestre do aluno: '))
		contagem += 1
		if contagem > 1:
			sys.exit('Estamos encerrando devido a inclusão errada de dados!')
	somanotas = nota1 + nota2 + nota3 + nota4
	media = somanotas / 4
	if media >= 7:
		print('{} foi aprovado com nota: {}'.format(aluno, media))
	else:
		print('{} foi reprovado com nota: {}'.format(aluno, media))

except ValueError:
	print('Valor diferente do solicitado')