#Дано трехзначное число. В нем зачеркнули первую слева цифру и приписали ее справа. Вывести.
number = int(input("Введите трёхзначное число: "))
if 99<number<1000:
    number_1 = number // 100
    number_2 = (number // 10) % 10
    number_3 = number % 10
    re_number = number_2 * 100 + number_3 * 10 + number_1
    print ("Вышло: " + str(re_number))
else:
    print("Вы ввели не трёхзначное число, перезапустите программу и попробуйте заново")


