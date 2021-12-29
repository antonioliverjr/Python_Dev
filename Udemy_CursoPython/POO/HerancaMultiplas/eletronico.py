class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self.__ligado = False

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def ligado(self):
        return self.__ligado

    def ligar(self):
        if self.__ligado:
            return
        self.__ligado = True
        print(f'{self.nome} Ligado!')

    def desligar(self):
        if not self.__ligado:
            return
        self.__ligado = False
        print(f'{self.nome} Desligado!')
