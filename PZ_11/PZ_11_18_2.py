# 2. Из предложенного текстового файла (text18-18.txt) вывести на экран его содержимое,
# количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в
# который поместить текст в стихотворной форме выведя строки в обратном порядке.

with open("text18-18.txt", 'r', encoding="utf-16") as file:
    lines = file.readlines()

count = 0
for line in lines[:4]:
    for i in line:
        if i in '.,?!:;—…':
            count+=1

print("Содержимое файла:")
for line in lines:
    print(line, end="")
print("\n Количество знаков пунктуации в первых четырёх строках:", count)

with open('reverse.txt', 'w', encoding="utf-16") as new_file:
    for line in reversed(lines):
        new_file.write(line)