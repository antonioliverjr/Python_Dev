from flask import Flask, render_template
from model import Movies


app = Flask(__name__)

@app.route('/')
def index():
    data = Movies()
    models = data.getList()
    if len(models) != 0:
        models = [
            {
                'name': x[0],
                'type_name': x[1],
                'total_ep': x[2],
                'atual_ep': x[3],
                'last_view': x[4].strftime('%d-%m-%Y')
            } for x in models
        ]
    else:
        models = [
            {
                'name': '',
                'type_name': '',
                'total_ep': '',
                'atual_ep': '',
                'last_view': ''
            }
        ]
    return render_template('index.html', models=models)

if __name__ == '__main__':
    app.run(debug=True)