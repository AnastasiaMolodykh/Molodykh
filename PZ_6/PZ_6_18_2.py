#2. Дано число R и список размера N. Найти два различных элемента списка, сумма
#которых наиболее близка к числу R, и вывести эти элементы в порядке возрастания
#их индексов (определение наиболее близких чисел - то есть такой элемент AK, для
#которого величина |AK - R| является минимальной).
import random
def closest_numbers(R, lst):
    index1 = 0
    index2 = 0
    min_diff = abs(lst[0] + lst[1] - R)
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            diff = abs(lst[i] + lst[j] - R)
            if diff < min_diff:
                index1 = i
                index2 = j
                min_diff = diff
    return index1, index2

R = int(input("Введите число R: "))
while type(R) != int:
    try:
        R = int(R)
    except ValueError:
       print("Неправильно ввели!")
       R = int(input("Введите число R: "))
lst = []
N = int(input("Введите размер списка: "))
for i in range(N):
    lst.append(random.randint(0, 20))
print(lst)
result = closest_numbers(R, lst)

print("Индекс пары наиболее близких элементов:", result)