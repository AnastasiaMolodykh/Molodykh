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
a = 1
x = 1
k = 1
while k <= number_n:
    while a > 1:
        a *= number_n
        number_n -= 1
        x += ((number_x ** number_n) / a)
    k += 1

print(x)


