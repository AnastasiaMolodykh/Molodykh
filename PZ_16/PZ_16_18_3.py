# Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
# сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации объектов Python в
# бинарном формате.

import pickle

from math import pi
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def length(self):
        return 2 * pi * self.radius

    def diameter(self):
        return 2 * self.radius

def save_def(circles, filename):
    with open(filename, 'wb') as file:
        pickle.dump(circles, file)

def load_def(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

circle1 = Circle(5)
circle2 = Circle(7)
circle3 = Circle(10)

print("Круг 1:")
print("Площадь:", circle1.area())
print("Длина окружности:", circle1.length())
print("Диаметр:", circle1.diameter())

print("\nКруг 2:")
print("Площадь:", circle2.area())
print("Длина окружности:", circle2.length())
print("Диаметр:", circle2.diameter())

print("\nКруг 3:")
print("Площадь:", circle3.area())
print("Длина окружности:", circle3.length())
print("Диаметр:", circle3.diameter())

circles = [circle1, circle2, circle3]
save_def(circles, "circles.bin")

loaded_circles = load_def("circles.bin")
print("\nЗагруженные круги:")
for circle in loaded_circles:
    print("Площадь:", circle.area())
    print("Длина окружности:", circle.length())
    print("Диаметр:", circle.diameter())