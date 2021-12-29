from classes.conta import Conta

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print(f'Saldo Insuficiente')
            return
        self.saldo -= valor
        self.detalhes()
