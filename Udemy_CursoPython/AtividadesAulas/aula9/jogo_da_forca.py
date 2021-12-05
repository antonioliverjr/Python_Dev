import os
import random

global acertos, palavra

def palavrasIniciais():
    if os.path.exists("palavras.txt"):
        pass
    else:
        with open("palavras.txt", "w") as file:
            file.write('DESENVOLVIMENTO;UM MUNDO DE MALUCOS...;ONDE SUA VIDA SE RESUMI A LER LETRAS...;ALGUNS SÃO VICIADOS EM CAFÉ E ENERGETICOS!'+'\n')
        with open("palavras.txt", "a") as file:
            file.write('PYTHON;UTILIZADA COMO RECURSO NO MUNDO DIGITAL;É UMA DAS MAIS UTILIZADAS NA SUA ÁREA;ESSE JOGO FOI FEITO COM ELA'+'\n')
            file.write('CARRO;USADO PARA LOCOMOÇÃO;É UM TIPO DE VEÍCULO;É O MAIS USADO NO MEIO URBANO'+'\n')
            file.write('CARNAVAL;FESTA FAMOSA NO BRASIL;ATRAI MUITOS TURISTAS PARA AS CAPITAIS QUE A COMEMORAM;ESTÁ ENTRE OS PRINCIPAIS EVENTOS ADIADOS NA PANDEMIA'+'\n')

def gravarPalavraSecreta(palavra, dica1, dica2, dica3):
    if palavra == '' or len(palavra) < 5 or dica1 == '' or len(dica1) < 10\
            or dica2 == '' or len(dica2) < 10 or dica3 == '' or len(dica3) < 10:
        return False
    elif consultaPalavras(palavra.upper()):
        return False
    else:
        texto = f'{palavra.upper()};{dica1.upper()};{dica2.upper()};{dica3.upper()}'
        with open("palavras.txt", "a") as file:
            file.write(texto+'\n')
        return True

def formPalavraSecreta():
    palavra_secreta = input("Digita a palavra secreta, com pelo menos 5 letras: ")
    dicaPalavra1 = input("Digite a 1º Dica, com pelo menos 10 letras: ")
    dicaPalavra2 = input("Digite a 2º Dica, com pelo menos 10 letras: ")
    dicaPalavra3 = input("Digite a 3º Dica, com pelo menos 10 letras: ")
    return gravarPalavraSecreta(palavra_secreta, dicaPalavra1, dicaPalavra2, dicaPalavra3)

def verificaAcertos(palavra, acertos):
    result = 0
    for x in palavra:
        if x in acertos:
            result += 1
        else:
            result -= 1
    return result

def pegarPalavraSecreta():
    with open("palavras.txt", "r") as pal:
        arquivo = pal.readlines()
    linha = arquivo[random.randint(0, (len(arquivo)-1))].replace('\n', '').split(';')
    palavra_secreta = linha[0].upper()
    return palavra_secreta

def pegarDica(palavra, num):
    with open("palavras.txt", "r") as pal:
        arquivo = pal.readlines()
    linha = []
    for lin in arquivo:
        textos = lin.replace('\n', '').split(';')
        if textos[0] == palavra:
            linha += textos
    dica = linha[num].upper()
    return dica

def consultaPalavras(palavra):
    with open("palavras.txt", "r") as pal:
        arquivo = pal.readlines()
    result = False
    for lin in arquivo:
        textos = lin.replace('\n', '').split(';')
        if textos[0] == palavra:
            result = True
            break
    return result

def main():
    palavra = pegarPalavraSecreta()
    qtd_letras = len(palavra)
    acertos = []
    digitadas = []
    chances = 1
    exibicao_palavra = ''
    log_mensagens = ''
    result = False

    while chances <= 6:
        os.system('cls' if os.name == 'nt' else 'clear')
        if chances == 1:
            print(f'##### {exibicao_palavra:*>{qtd_letras}} #####')
        elif chances == 2:
            print('''
    +----+
    |    |
    |    O
    |
    |
    |
                  ''')
            print()
            print('##### {} #####'.format(exibicao_palavra))
        elif chances == 3:
            print('''
    +----+
    |    |
    |    O
    |    |
    |
    |              
                  ''')
            print('##### {} #####'.format(exibicao_palavra))
            print()
        elif chances == 4:
            print('''
    +----+
    |    |
    |   (O
    |    |
    |
    |
                  ''')
            print()
            print('##### {} #####'.format(exibicao_palavra))
        elif chances == 5:
            print('''
    +----+
    |    |
    |   (O)
    |    |
    |
    |
                  ''')
            print()
            print('##### {} #####'.format(exibicao_palavra))
        elif chances == 6:
            print('''
    +----+
    |    |
    |   (O)
    |    |
    |   /
    |
                  ''')
            print()
            print('##### {} #####'.format(exibicao_palavra))

        print()
        print(log_mensagens)
        print(f'A palavra secreta tem {qtd_letras} letras...')
        print(f'Você ainda tem {6-chances} chances...')
        if chances == 3:
            print()
            print(f'Vamos lá! Uma dica - {pegarDica(palavra, 1)}')
        elif chances == 4:
            print()
            print(f'Vamos lá! 1º dica - {pegarDica(palavra, 1)}')
            print(f'2º dica - {pegarDica(palavra, 2)}')
        elif chances == 5:
            print()
            print(f'Vamos lá! 1º dica - {pegarDica(palavra, 1)}')
            print(f'2º dica - {pegarDica(palavra, 2)}')
            print(f'3º dica - {pegarDica(palavra, 3)}')
        elif chances == 6:
            print()
            print(f'Vamos lá! 1º dica - {pegarDica(palavra, 1)}')
            print(f'2º dica - {pegarDica(palavra, 2)}')
            print(f'3º dica - {pegarDica(palavra, 3)}')
            print('Ultima chance, vamos lá!')

        print()
        letra = input("Digite uma letra: ").upper()

        if letra in digitadas:
            log_mensagens = 'Essa letra já foi digitada, informe uma letra diferente de '
            for i in digitadas:
                log_mensagens += ', '+ i
            log_mensagens += '...'
            continue

        if len(letra) > 1:
            print()
            print('Isso não é permitido, digite apenas uma letra...')
            chute = input('Ou se deseja chutar digite "S": ').upper()
            if chute == 'S':
                if letra == palavra:
                    for x in letra:
                        acertos += x
                    result = verificaAcertos(palavra, acertos)
                    break
                else:
                    chances = 7
            else:
                continue

        digitadas.append(letra)

        if letra in palavra:
            log_mensagens = 'Muito bem! a letra '+ letra +' existe na palavra secreta!'
            print()
            acertos.append(letra)
        else:
            log_mensagens = 'Vixe! A letra '+ letra +' não existe na palavra secreta.'
            print()
            chances += 1

        exibicao_palavra = ''
        for letra_secreta in palavra:
            if letra_secreta in acertos:
                exibicao_palavra += letra_secreta
            else:
                exibicao_palavra += '*'

        result = verificaAcertos(palavra, acertos)

        if result == len(palavra):
            break
        else:
            continue

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''
    +----+
    |    |
    |    0 
    |   /|\\
    |   / \\
    |
                      ''')
        print()
        print('Suas chances esgotaram! Game Over!')

    if result == len(palavra):
        print()
        print('Parabéns, você ganhou!')
        print(f'A palavra secreta foi {palavra.upper()}')
        print()
        aceita_gravar = input("""Como ganhou pode cadastrar uma palavra para desafiar alguém!
Caso deseje, é simples além da palavra deve dar 3 dicas, digite 'S' para cadastrar: """)
        print()

        if aceita_gravar.upper() == 'S':
            result = formPalavraSecreta()
            if result:
                print("Cadastro realizado com sucesso!")
            else:
                print("Opss, alguma informação ficou pendente ou já existe essa palavra, não podemos cadastrar!")

        reiniciar = input("Deseja jogar novamente 'S' ou 'N'? ").upper()

        if reiniciar == 'S':
            main()

if __name__ == "__main__":
    palavrasIniciais()
    main()