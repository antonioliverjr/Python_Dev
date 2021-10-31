from flask import Flask
from flask_restful import Api
from habilidades import ListaHabilidades ,Habilidades
from desenvolvedores import ListaDesenvolvedores, Desenvolvedor

app = Flask(__name__)
api = Api(app)

api.add_resource(ListaDesenvolvedores, '/dev')
api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(Habilidades,  '/habilidades/<int:id>')
api.add_resource(ListaHabilidades, '/habilidades')

if __name__ == '__main__':
    app.run(debug=True)
