# Создание базового класса "Транспортное средство" и его наследование для создания
# классов "Автомобиль" и "Мотоцикл". В классе "Транспортное средство" будут
# общие свойства, такие как максимальная скорость и количество колес, а классы-наследники
# будут иметь свои уникальные свойства и методы.

class Transport:
    max_speed = ''
    kolvo_koles = ''

class Car(Transport):

    def __init__(self, color, pyt, time):
        self.color = color
        self.pyt = pyt
        self.time = time

    def avto(self):
        print('Максимальная скорость данного автомобиля: ', self.max_speed)
        print('Количество колес автомобиля: ', self.kolvo_koles)
    def rate(self):
        S = self.pyt
        t = self.time
        V = S / t
        print("Скорость автомобиля в данной поездке: ", V)

class Motorcycle(Transport):
    def __init__(self, massa, speed, time):
        self.massa = massa
        self.speed = speed
        self.time = time

    def mot(self):
        print('Максимальная скорость данного мотоцикла: ', self.max_speed)
        print('Количество колес мотоцикла: ', self.kolvo_koles)

    def way(self):
        v = self.speed
        t = self.time
        S = v * t
        print("Данный мотоцик проехал: ", S)

avt = Car()

