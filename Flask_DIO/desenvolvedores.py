from flask import request, make_response
from flask_restful import Resource
from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields
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

@doc(tags=['Desenvolvedores Atualizações'])
class Desenvolvedor(MethodResource, Resource):
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

class DesenvolvedoresResponseSchema(Schema):
    message = fields.Str(default='Sucess')
class DesenvolvedoresRequestSchema(Schema):
    nome = fields.String(required=True, description='Informe o nome do desenvolvedor')
    habilidades = fields.List(fields.String(description='Informa habilidade do desenvolvedor'))
class DesenvolvedoresRequestFailSchema(Schema):
    message = fields.Str(default='Error')

@doc(tags=['Desenvolvedores'])
class ListaDesenvolvedores(MethodResource, Resource):
    @doc(description='Adicione um desenvolvedor')
    @use_kwargs(DesenvolvedoresRequestSchema, location='json')
    @marshal_with(DesenvolvedoresResponseSchema, code=200, description='Cadastrado com sucesso.')
    @marshal_with(DesenvolvedoresRequestFailSchema, description='Erro ao cadastrar', code=400)
    @marshal_with(DesenvolvedoresRequestFailSchema, description='Campos Nulos', code=422)
    def post(self, **kwargs):
        try:
            dados = json.loads(request.data)
            if(dados is None):
                response = make_response('', 422)
                return response

            if(dados['nome'] is None or dados['nome'] == ''):
                response = make_response('', 400)
                return response

            posicao = len(desenvolvedores)
            dados['id'] = int(posicao) + 1
            desenvolvedores.append(dados)
            return desenvolvedores[posicao]
        except Exception:
            messagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status':'error', 'mensagem':messagem}
            return response
    @doc(description='Lista Desenvolvedores')
    #@marshal_with(DesenvolvedoresResponseSchema)
    def get(self):
        return desenvolvedores
