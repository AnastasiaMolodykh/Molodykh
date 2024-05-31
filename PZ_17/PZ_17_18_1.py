# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 2 – 9.
# Задача из ПЗ 3. Дано целое положительное число. Проверить истинность высказывания: «Данное число является нечетным трехзначным».

import tkinter as tk
from tkinter import messagebox

def check_number():
    try:
        number = int(entry.get())
        if number % 2 != 0 and (number // 100 <= 10 and number // 100 != 0):
            result = "Истинность высказывания верна! Данное число является нечетным и трехзначным."
        elif number % 2 != 0 and (number // 100 > 10 or number // 100 < 0):
            result = "Истинность высказывания неверна! Данное число является нечетным и не трехзначным."
        elif number % 2 == 0 and (number // 100 <= 10 and number // 100 != 0):
            result = "Истинность высказывания неверна! Данное число является четным и трехзначным."
        else:
            result = "Истинность высказывания неверна! Данное число является четным и не трехзначным."
        messagebox.showinfo("Результат", result)
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите целое число.")

root = tk.Tk()
root.title("Проверка числа")

label = tk.Label(root, text="Введите целое положительное число:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Проверить", command=check_number)
button.pack(pady=10)

root.mainloop()