# Создание базового класса "Транспортное средство" и его наследование для создания
# классов "Автомобиль" и "Мотоцикл". В классе "Транспортное средство" будут
# общие свойства, такие как максимальная скорость и количество колес, а классы-наследники
# будут иметь свои уникальные свойства и методы.

class Transport:
    def __init__(self, max_speed, num_wheels):
        self.max_speed = max_speed
        self.num_wheels = num_wheels

class Car(Transport):
    def __init__(self, max_speed, num_wheels, path, time):
        super().__init__(max_speed, num_wheels)
        self.path = path
        self.time = time

    def calculate_speed(self):
        if self.time > 0:
            return self.path / self.time
        else:
            return 0

    def describe(self):
        speed = self.calculate_speed()
        return f"Автомобиль: максимальная скорость: {self.max_speed} км/ч, количество колёс: {self.num_wheels}, путь: {self.path} км, время:: {self.time} ч, расчетная скорость: {speed} км/ч."

class Motorcycle(Transport):
    def __init__(self, max_speed, num_wheels, speed, time):
        super().__init__(max_speed, num_wheels)
        self.speed = speed
        self.time = time

    def calculate_path(self):
        return self.speed * self.time

    def describe(self):
        path = self.calculate_path()
        return f"Мотоцикл: максимальная скорость: {self.max_speed} км/ч, количество колёс:{self.num_wheels}, скорость: {self.speed} км/ч, время: {self.time} ч, расчетный путь: {path} км."

car = Car(180, 4, 400, 4)
print(car.describe())

motorcycle = Motorcycle(200, 2, 85, 3)
print(motorcycle.describe())