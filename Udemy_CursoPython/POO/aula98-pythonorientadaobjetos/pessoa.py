from datetime import datetime
from random import randint

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}'

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return
        if self.falando:
            print(f'{self.nome} já está falando ...')

        print(f'{self.nome} diz: {assunto}')
        self.falando = True

    def pararFalar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return

        print(f'{self.nome} parou de falar ...')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo!')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando!')
            return

        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    def paraComer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo!')
            return

        print(f'{self.nome} parou de comer!')
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade

    @classmethod
    def por_ano_nascimento(cls, nome, ano_de_nascimento):
        idade = cls.ano_atual - ano_de_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand
