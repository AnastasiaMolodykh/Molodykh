#1. Составить программу, в которой функция генерирует четырехзначное число и
#определяет, есть ли в числе одинаковые цифры.
import random
def num():
    number = random.randint(1000, 9999)
    print(number)
    chislo = set(str(number))
    if len(chislo) < 4:
        return True
    else:
        return False
res = num()
if res:
    print("В числе есть одинаковые цифры")
else:
    print("В числе нет одинаковых цифр")