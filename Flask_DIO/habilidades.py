from flask_restful import Resource
from flask import request
import json

lista_habilidades = [
        'Python',
        'Java',
        'C#',
        'PHP',
        'Flash',
        'Django',
        'Laravel',
        'NET'
]

class ListaHabilidades(Resource):
    def get(self):
        listagem = []
        indice = 1
        for habilidade in lista_habilidades:
            listagem.append({f'{indice}':f'{habilidade}'})
            indice += 1
        return listagem
    def post(self):
        dados = json.loads(request.data)
        if dados['habilidade'] not in lista_habilidades:
            lista_habilidades.append(dados['habilidade'])
            return lista_habilidades
        return 'Habilidade já consta na lista'

class Habilidades(Resource):
    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id-1] = dados['habilidade']
        return lista_habilidades

    def delete(self, id):
        lista_habilidades.pop(id-1)
        return lista_habilidades