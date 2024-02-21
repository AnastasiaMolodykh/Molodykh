# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Среднее арифметическое элементов:
# Последовательность, в которой каждый последующий элемент равен квадрату суммы двух
# соседних элементов:

spisok = ['-1 2 1 -2 4 3 -2']
f_1 = open('data.txt', 'w')
f_1.writelines(spisok)
f_1.close()

f_2 = open('data_copy.txt', 'w')
f_2.write('Исходные данные: ')
f_2.writelines(spisok)
f_2.write('\n')
f_2.close()

f_1 = open('data.txt')
k = f_1.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f_1.close()

f_2 = open('data_copy.txt', 'a')
kolvo = str(len(k))
f_2.write('Количество элементов: ')
f_2.writelines(kolvo)
f_2.write('\n')
f_2.close()

f_2 = open('data_copy.txt', 'a')
sr_ar = str(sum(k)/int(kolvo))
f_2.write('Среднее арифметическое элементов: ')
f_2.writelines(sr_ar)
f_2.write('\n')
f_2.close()

f_2 = open('data_copy.txt', 'a')
one_first = [(k[1])**2]
one_last = [(k[-2])**2]
n = []
for i in range(1, len(k)-1):
    n.append(((k[i-1] + k[i+1]) ** 2))
itog = one_first+n+one_last
f_2.write('Последовательность, в которой каждый последующий элемент равен квадрату суммы двух соседних элементов: ')
f_2.writelines(str(itog))
f_2.close()




