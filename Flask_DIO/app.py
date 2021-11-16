from flask import Flask
from flask_restful import Api
from habilidades import ListaHabilidades, Habilidades
from desenvolvedores import ListaDesenvolvedores, Desenvolvedor

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec

app = Flask(__name__)
api = Api(app)

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Desenvolvedores API',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger-json/',
    'APISPEC_SWAGGER_UI_URL': '/swagger/'
})

docs = FlaskApiSpec(app)

api.add_resource(ListaDesenvolvedores, '/dev')
docs.register(ListaDesenvolvedores)
api.add_resource(Desenvolvedor, '/dev/<int:id>')
docs.register(Desenvolvedor)
api.add_resource(Habilidades,  '/habilidades/<int:id>')
api.add_resource(ListaHabilidades, '/habilidades')

if __name__ == '__main__':
    app.run(debug=True)
