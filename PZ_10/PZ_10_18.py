# Имеется список студентов группы, в котором все имена различны. Определить, есть ли в
# группе студент, который побывал в гостях у всех студентов. (Для каждого студента
# составить список из множества побывавших у него в гостях друзей, причем хозяина в этот
# список не включать).
Oleg = {'Irina'}
Irina = {'Olga'}
Olga ={'Irina','Oleg'}
if Oleg&Olga != set():
    print('У всех в гостях был:', Oleg&Olga)
if Oleg&Irina != set():
    print('У всех в гостях был:', Oleg&Irina)
if Irina&Olga != set():
    print('У всех в гостях был:', Irina&Olga)