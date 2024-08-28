# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela
# comentario mediocre


class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None

    @property
    def motor(self):

        return self._motor

    @motor.setter
    def motor(self, motor):
        self._motor = motor


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self.carros = []

    def carrosFabricados(self, *carros):
        self.carros.extend(carros)

    def listarCarros(self):
        for car in self.carros:
            print(self.nome, car.nome, car.motor.nome)


if __name__ == '__main__':

    motorv8 = Motor('motor_v8')
    carro1 = Carro("c4 pallas")
    carro2 = Carro('c4 ')
    carro1.motor = motorv8
    carro2.motor = Motor('motor_v6')
    fabricante = Fabricante("citroen")
    fabricante.carrosFabricados(carro1, carro2)

    fabricante1 = Fabricante('chev')
    carro3 = Carro('impala')
    carro3.motor = motorv8
    fabricante1.carrosFabricados(carro3)

    fabricante.listarCarros()
    fabricante1.listarCarros()
