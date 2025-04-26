from abc import ABC, abstractmethod

class Veiculo(ABC):  # ABC = Abstract Base Class
    @abstractmethod
    def mover(self):
        pass

class Carro(Veiculo):
    def mover(self):
        print("O carro está andando...")

class Aviao(Veiculo):
    def mover(self):
        print("O avião está voando...")

transportes = [Carro(), Aviao()]
for t in transportes:
    t.mover()
