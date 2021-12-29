from zipfile import ZipFile
import os


caminho = r'arquivos'
with ZipFile('arquivo.zip', 'w') as file:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        file.write(caminho_completo, arquivo)

with ZipFile('arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

with ZipFile('arquivo.zip', 'r') as zips:
    zips.extractall('descompactado')
