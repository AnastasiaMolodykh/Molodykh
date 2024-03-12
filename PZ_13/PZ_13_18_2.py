# 2. В матрице найти среднее арифметическое элементов последних двух столбцов.

from functools import reduce

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

two_last = map(lambda row: row[-2:], matrix)
list_chis = reduce(lambda x, y: x + y, two_last)

sum_el = sum(list_chis)
kol = len(list_chis)
sr_ar = sum_el / kol

print("Среднее арифметическое элементов последних двух столбцов:", sr_ar)