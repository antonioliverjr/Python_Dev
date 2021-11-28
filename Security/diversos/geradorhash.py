import hashlib

string = input("Digite o text a ser gerado a hash: ")

menu = int(input(''' #### MENU - ESCOLHA O TIPO DE HASH ####
                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512
                Digite o número do hash a ser gerado: '''))

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    hash = 'MD5'
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    hash = 'SHA1'
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    hash = 'SHA256'
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    hash = 'SHA512'
else:
    print("Valor informado não possui hash correspondente...")

if menu == 1 or menu == 2 or menu == 3 or menu == 4:
    print(f'A hash {hash} da string é: {resultado.hexdigest()}')