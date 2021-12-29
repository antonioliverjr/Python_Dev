import os
import sys
import shutil


caminho_origem = r'C:\pasta_teste1'
caminho_destino = r'C:\Users\antoliverjr\Desktop\pasta_teste2'

try:
    os.mkdir(caminho_destino)
except FileExistsError as e:
    print(f'Pasta {caminho_destino} já existe')

for caminho, diretorios, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        caminho_antigo_arquivo = os.path.join(caminho, arquivo)
        nome, extensao = os.path.splitext(arquivo)
        novo_arquivo = nome + '_novo' + extensao
        caminho_novo_arquivo = os.path.join(caminho_destino, novo_arquivo)

        if 'python' in arquivo:
            shutil.copy(caminho_antigo_arquivo, caminho_novo_arquivo)
