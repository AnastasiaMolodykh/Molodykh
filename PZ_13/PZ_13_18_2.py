# 2. В матрице найти среднее арифметическое элементов последних двух столбцов.

from functools import reduce
import numpy as np

matrix = np.random.randint(10, size = (3,3))
print("Исходная матрица:")
print(matrix)

two_last = map(lambda row: row[-2:], matrix)
list_chis = reduce(lambda x, y: x + y, two_last)

sr_ar = sum(list_chis) / len(list_chis)

print("Среднее арифметическое элементов последних двух столбцов:", sr_ar)