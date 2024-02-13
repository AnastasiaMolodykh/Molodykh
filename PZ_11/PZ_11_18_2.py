# 2. Из предложенного текстового файла (text18-18.txt) вывести на экран его содержимое,
# количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в
# который поместить текст в стихотворной форме выведя строки в обратном порядке.
# myfile = open("text18-18.txt", "r")
# myline = myfile.readline()
# print(myline)
# myfile.close()

# d = 0
# for i in open('text18-18.txt', encoding='UTF-8'):
#     print(i, end='')
#     t += 1
#     for j in i:
#         if j == 'ж':
#         d += 1
# print(end='\n')
# print('Количество строк:    ', t, end='\n')
# print('Количество букв "ж" :    ', d, end='\n')

with open('text18-18.txt', 'r') as file:
    content = file.readlines()

# Вывод содержимого файла
print("Содержимое файла:")
for line in content:
    print(line.strip())

# Подсчет количества знаков пунктуации в первых четырех строках
punctuation_count = 0
for line in content[:4]:
    for char in line:
        if char in '.,?!:;-':
            punctuation_count += 1

print("\nКоличество знаков пунктуации в первых четырёх строках:", punctuation_count)

with open('новый_файл.txt', 'w') as new_file:
    new_file.writelines(reversed(content))
