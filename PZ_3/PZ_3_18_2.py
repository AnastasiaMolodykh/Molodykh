#2. Даны три числа. Найти среднее из них (то есть число, расположенное между наименьшим и наибольшим).
number_1 = input("Введите первое число: ")              #Ввод трёх чисел
number_2 = input("Введите второе число: ")
number_3 = input("Введите третье число: ")
while type(number_1) != int:                            # обработка исключений
    try:
        number_1 = int(number_1)
    except ValueError:
        print("Неправильно ввели!")
        number_1 = input("Введите первое число: ")

while type(number_2) != int:                          # обработка исключений
    try:
        number_2 = int(number_2)
    except ValueError:
        print("Неправильно ввели!")
        number_2 = input("Введите второе число: ")

while type(number_3) != int:                          # обработка исключений
    try:
        number_3 = int(number_3)
    except ValueError:
        print("Неправильно ввели!")
        number_3 = input("Введите третье число: ")

if number_1 > number_2 and number_1 > number_3 and number_2 > number_3:  #Проверка условий
    print("Среднее число: ", number_2)
elif number_2 > number_1 and number_2 > number_3 and number_1 > number_3:
    print("Среднее число: ", number_1)
else:
    print("Среднее число: ", number_3)