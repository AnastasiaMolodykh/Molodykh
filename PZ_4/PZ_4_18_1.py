#1. Дано вещественное число X и целое число N (> 0). Найти значение выражения 1 + X + X^2/(2!) + ... + X^N/(N!) (N! = 12 ...N). Полученное число является приближенным
#значением функции exp в точке X.
number_x = input("Введите вещественное число:")
while type(number_x) != float:                      # обработка исключений
    try:
        number_x = float(number_x)
    except ValueError:
       print("Неправильно ввели!")
       number_x = input("Введите вещественное число: ")

number_n = input("Введите целое число:")
while type(number_n) != int:                        # обработка исключений
    try:
        number_n = int(number_n)
    except ValueError:
       print("Неправильно ввели!")
       number_n = input("Введите целое число: ")
while number_n < 0:
    print("Вы ввели отрицательное число! Попробуйте снова!")
    number_n = int(input("Введите целое число: "))
x = 1
factorial = 1
for i in range(1, number_n + 1):
    for j in range(1, i + 1):
        factorial *= j
    x += (number_x ** i) / factorial
print(x)


