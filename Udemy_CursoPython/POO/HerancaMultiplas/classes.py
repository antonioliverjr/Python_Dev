class A:
    def falar(self):
        print('falando... Estou em A.')

class B(A):
    def falar(self):
        print('falando... Estou em B.')

class C(A):
    def falar(self):
        print('falando... Estou em C.')

class D(B, C):
    pass
