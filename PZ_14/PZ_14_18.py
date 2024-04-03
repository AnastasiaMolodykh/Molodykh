# Из исходного текстового файла (expansion.txt) выбрать имена фалов,
# соответствующие типам: .xls, .xml, .html, .css, .py.Посчитать количество полученных
# элементов.
import re

with open('expansion.txt', 'r') as file:
    data = file.read()

imena = re.findall(r'\b\w+\.(?:xls|xml|html|css|py)\b', data)
kolvo = len(imena)

print('Имена файлов', imena)
print('Количество файлов', kolvo)