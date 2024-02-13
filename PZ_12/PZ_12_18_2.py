# 2. Составить  генератор  (yield),  который  преобразует  все  буквенные  символы  в
# строчные.
def lowercase(text):
    for i in text:
        if i.isalpha():
            yield i.lower()
        else:
            yield i

text = "Hello World!"
lowercase_text = ''.join(lowercase(text))
print(lowercase_text)