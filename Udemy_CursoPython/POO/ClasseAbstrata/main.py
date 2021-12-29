# class A(ABC):
#     @abstractmethod
#     def falar(self):
#         pass
#
# class B(A):
#     def falar(self):
#         print('Falando... B...')
#
# a = B()

from classes.conta_poupanca import ContaPoupanca
from classes.conta_corrente import ContaCorrente

cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(50)
cp.sacar(10)

cc = ContaCorrente(1111, 3333, 0, 500)
cc.depositar(100)
cc.sacar(300)
cc.depositar(1000)
