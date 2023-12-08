#3.   Дан  список  размера  N,  все  элементы  которого,  кроме  первого,  упорядочены  по
#возрастанию. Сделать список упорядоченным, переместив первый элемент на новую
#позицию.

my_list =[65, 19, 38, 49, 57, 62, 73,86, 92, 123, 159, 187]
print("Исходный список: ", my_list)
new_list = []
new_list.append(my_list[0])
for i in range(len(my_list)):
    if my_list[i]<my_list[0]:
        new_list.insert(i,my_list[i])
    else:
        new_list.insert(i+1,my_list[i])
new_list.pop(0)
print("Итоговый список: " , new_list)
