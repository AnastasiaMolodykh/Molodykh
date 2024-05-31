# Задание предполагает, что у студента есть проект с практическими работами (№№ 2-13),
# оформленный согласно требованиям. Все задания выполняются c использованием модуля
# OS:
#   перейдите в каталог PZ11.  Выведите  список  всех  файлов  в  этом  каталоге.  Имена
# вложенных подкаталогов выводить не нужно.
#   перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
# test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
# Файл  из  ПЗ7  переименовать в  test.txt.  Вывести  в  консоль  информацию  о  размере
# файлов в папке test.
#   перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
# консоль. Использовать функцию basename () (os.path.basename()).
#   перейти  в  любую  папку  где  есть  отчет  в  формате  .pdf  и  «запустите»  файл  в
# привязанной к нему программе. Использовать функцию os.startfile().
#   удалить файл test.txt.

import os

os.chdir(r'C:\Users\Анастасия\Documents\Molodykh\PZ_11')
print(os.listdir())

os.chdir('..')

os.makedirs('test/test1')

os.replace('PZ_6/PZ_6_18_1.py', 'test/PZ_6_18_1.py')
os.replace('PZ_6/PZ_6_18_2.py', 'test/PZ_6_18_2.py')
os.replace('PZ_7/PZ_7_18_2.py', 'test/test1/PZ_7_18_2.py')

os.rename("test/test1/PZ_7_18_2.py", "test/test1/test.txt")

print("Размер файлов в папке test:")
for item in os.listdir('test'):
    file_path = os.path.join('test', item)
    if os.path.isfile(file_path):
        print(f"{item}: {os.path.getsize(file_path)} байт")

os.chdir(r'C:\Users\Анастасия\Documents\Molodykh\PZ_11')
shortest_name = min((f for f in os.listdir('.') if os.path.isfile(f)), key=len)
print("Файл с самым коротким именем в PZ_11:", os.path.basename(shortest_name))

os.chdir(r'C:\Users\Анастасия\Documents\Molodykh\reports')
os.startfile('ПЗ_9.pdf')

os.chdir("..")
os.remove("test/test1/test.txt")