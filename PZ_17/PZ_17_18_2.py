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

os.chdir('PZ11')
print("Список файлов в каталоге PZ11:")
for item in os.listdir('.'):
    if os.path.isfile(item):
        print(item)

os.chdir('..')

os.makedirs('test/test1', exist_ok=True)

os.rename('PZ6/файл1.txt', 'test/файл1.txt')
os.rename('PZ6/файл2.txt', 'test/файл2.txt')

os.rename('PZ7/файл3.txt', 'test/test1/test.txt')

print("Размер файлов в папке test:")
for item in os.listdir('test'):
    file_path = os.path.join('test', item)
    if os.path.isfile(file_path):
        print(f"{item}: {os.path.getsize(file_path)} байт")

os.chdir('PZ11')
shortest_name = min((f for f in os.listdir('.') if os.path.isfile(f)), key=len)
print("Файл с самым коротким именем в PZ11:", os.path.basename(shortest_name))

pdf_folder = 'reports'
pdf_file = 'PZ_12.pdf'
pdf_path = os.path.join(pdf_folder, pdf_file)
if os.path.isfile(pdf_path):
    os.startfile(pdf_path)
else:
    print(f"Файл {pdf_file} не найден в папке {pdf_folder}")

os.remove('test/test1/test.txt')