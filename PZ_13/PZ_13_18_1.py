# 1. В матрице элементы кратные 3 увеличить в 3 раза

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
def three(num):
    if num % 3 == 0:
        return num * 3
    return num

new_matrix = list(map(lambda row: list(map(three, row)), matrix))

for i in new_matrix:
    print(i)