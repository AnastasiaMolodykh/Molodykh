# 1. В матрице элементы кратные 3 увеличить в 3 раза

import numpy as np

matrix = np.random.randint(10, size = (3,3))
print("Исходная матрица:")
print(matrix)
# def three(num):
#     if num % 3 == 0:
#         return num * 3
#     return num

# new_matrix = list(map(lambda row: list(map(three, row)), matrix))

new_matrix = list(map(lambda row: list(row * 3 if row % 3 == 0), matrix))

print("Итоговая матрица:")
for i in new_matrix:
    print(i)