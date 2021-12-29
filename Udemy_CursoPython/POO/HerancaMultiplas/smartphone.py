from eletronico import Eletronico
from log import LogMixin


class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self.__conectado = False

    def conectar(self):
        if not self.ligado:
            info = f'{self.nome} não está ligado'
            print(info)
            self.log_info(info)
            return

        if self.__conectado:
            error = f'{self.nome} JÁ ESTÁ CONECTADO'
            print(error)
            self.log_error(error)
            return

        self.__conectado = True
        print(f'{self.nome} Conectado!')

    def desconectar(self):
        if not self.__conectado:
            info = f'{self.nome} NÃO ESTÁ CONECTADO'
            print(info)
            self.log_info(info)
            return
        self.__conectado = False
        print(f'{self.nome} Desconectado!')
