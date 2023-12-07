#3.   Дан  список  размера  N,  все  элементы  которого,  кроме  первого,  упорядочены  по
#возрастанию. Сделать список упорядоченным, переместив первый элемент на новую
#позицию.

my_list =[8,1,2,3,5,7,9]
print(my_list)
elem = my_list.pop(0)
new_list = []
for i in my_list:
    if i>elem:
        new_list.append(elem)
    new_list.append(i)
print(new_list)