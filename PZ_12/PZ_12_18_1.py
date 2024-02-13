# 1.В  последовательности  на  n  целых  элементов  найти  произведение  элементов
# средней трети.
from functools import reduce

posled = int(input("Введите количество элементов: "))

a = []
for i in range(1,posled+1):
    a.append(i)
print(a)
r = len(a)//3
f = [a.pop(0) for i in range(r)]
f = [a.pop(-1) for i in range(r)]
print(a)

print(reduce(lambda x,y:x*y,a))