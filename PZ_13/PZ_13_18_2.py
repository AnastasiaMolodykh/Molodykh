# 2. В матрице найти среднее арифметическое элементов последних двух столбцов.

from functools import reduce
import random

matrix = [[random.randint(0,20) for _ in range(3)] for _ in range(3)]
print("Исходная матрица:")
for i in matrix:
    print(i)

two_last = map(lambda row: row[-2:], matrix)
list_chis = reduce(lambda x, y: x + y, two_last)

sr_ar = sum(list_chis) / len(list_chis)

print("Среднее арифметическое элементов последних двух столбцов:", sr_ar)