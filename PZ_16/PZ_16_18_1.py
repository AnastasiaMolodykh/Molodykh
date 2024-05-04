# Создайте класс «Круг», который имеет атрибут радиуса и методы для вычисления
# площади, длины окружности и диаметра.
from math import pi
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        S = pi * self.radius**2
        print("Площадь равна: ", S)

    def length(self):
        C = 2 * pi * self.radius
        print("Длина окружности равна: ", C)

    def diametr(self):
        D = 2 * self.radius
        print("Диаметр равен: ", D)

circle = Circle(5)
circle.area()
circle.length()
circle.diametr()
print(circle.__dict__)