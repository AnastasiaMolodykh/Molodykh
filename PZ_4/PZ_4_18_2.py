#2. Даны целые положительные числа A и B (A < B). Вывести все целые числа от A до
#B включительно; при этом каждое число должно выводиться столько раз, каково его
#значение (например, число 3 выводится 3 раза).
a, b = input("Введите первое число: "), input("Введите второе число: ")
while type(a) != int: # обработка исключений
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите первое число: ")
while type(b) != int: # обработка исключений
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите второе число: ")
if a < b:
    k = a
    while a <= b:
        print(str(a)*k)
        a += 1
        k += 1
else:
    print("Ошибка! Попробуйте снова!")
