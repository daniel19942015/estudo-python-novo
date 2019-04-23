class Carro():

    def __init__(self, cor, roda = None):
        self.roda = roda
        self.cor = cor

    def getRoda(self):
        return self.roda

    def getCor(self):
        return self.cor

carro = Carro("Azul", "Aro 15")

print(carro.getRoda())
print(carro.getCor())