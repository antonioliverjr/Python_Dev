"""
Testando developer mobile Python
"""
from typing import Text
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import requests
import json


class AppFuturo(toga.App):

    def startup(self):

        main_box = toga.Box(style=Pack(direction=COLUMN))
        main_box.add(
            toga.Label("Cadastre-se")
        )
        self.Login = toga.TextInput(placeholder='Informe seu Login...')
        main_box.add(
            self.Login
        )
        self.Senha = toga.PasswordInput(placeholder='Digite a senha cadastrada...')
        main_box.add(
            self.Senha
        )
        main_box.add(
            toga.Button('Logar', on_press=self.enviar)
        )

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def enviar(self, widget):
        resultado = self.Logar(self) 
        '''
        ApiKey = resultado['token']
        Login = resultado['usuario']['login']
        Email = resultado['usuario']['email']
        if(ApiKey != ''):
            self.main_window.info_dialog('Cadastro', f'Seja Bem Vindo {Login}!')
        app = toga.Box()
        app.add(
            toga.Label('Cadastrado'),
            toga.Label(f'{ApiKey}'),
            toga.Label(f'{Login}'),
            toga.Label(f'{Email}')
        )
        self.main_window.content = app
        '''

    def Logar(self, widget):
        dados = {
            "login": self.Login.value,
            "senha": self.Senha.value
        }
        headers = {
            'accept': 'text/plain',
            'content-type': 'application/json'
        }
        data = json.dumps(dados)
        response = requests.post('https://localhost:1698/api/v1/usuario/logar', headers=headers, data=data, verify=False)
        return json.loads(response)
    '''
    def toJSON(self, widget):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    '''
def main():
    return AppFuturo()
