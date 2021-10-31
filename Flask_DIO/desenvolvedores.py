from flask import request
from flask_restful import Resource
import json

desenvolvedores = [
    {
        'id': 1,
        'nome': 'Antonio',
        'habilidades': [
            'Python',
            'C#',
            'T-SQL'
        ]
    }
]


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            desenvolvedor = desenvolvedores[id-1]
            return desenvolvedor
        except IndexError:
            messagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem':messagem}
        except Exception:
            messagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': messagem}
        return response

    def put(self, id):
        try:
            dados = json.loads(request.data)
            desenvolvedores[id-1] = dados
            return dados
        except IndexError:
            messagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': messagem}
        except Exception:
            messagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': messagem}
        return response
    def delete(self, id):
        try:
            nome = desenvolvedores[id-1]['nome']
            desenvolvedores.pop(id-1)
            response = 'Desenvolvedor {} foi deletado com sucesso!'.format(nome)
            return response
        except IndexError:
            messagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': messagem}
        except Exception:
            messagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': messagem}
        return response

class ListaDesenvolvedores(Resource):
    def post(self):
        try:
            dados = json.loads(request.data)
            posicao = len(desenvolvedores)
            dados['id'] = int(posicao) + 1
            desenvolvedores.append(dados)
            return desenvolvedores[posicao]
        except Exception:
            messagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status':'error', 'mensagem':messagem}
            return response
    def get(self):
        return desenvolvedores