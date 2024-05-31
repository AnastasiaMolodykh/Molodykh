# 1. В матрице элементы кратные 3 увеличить в 3 раза

import random

matrix = [[random.randint(0,20) for _ in range(3)] for _ in range(3)]
print("Исходная матрица:")
for i in matrix:
    print(i)

new_matrix = list(map(lambda row: list(map(lambda x: x * 3 if x % 3 == 0 else x, row)), matrix))

print("Итоговая матрица:")
for i in new_matrix:
    print(i)