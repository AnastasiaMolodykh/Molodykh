# Приложение СТРАХОВАЯ КОМПАНИЯ для некоторой организации. БД должна
# содержать таблицу Договор со следующей структурой записи: дата заключения, страховая
# сумма, вид страхования, тарифная ставка и филиал, в котором заключался договор.

import sqlite3 as sq
from data import info

with sq.connect('Insurance_Company.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS contract")
    cur.execute("""CREATE TABLE IF NOT EXISTS contract (
    date_start TEXT NOT NULL,
    insurance_sum INTEGER NOT NULL,
    insurance_type TEXT NOT NULL,
    tariff_rate INTEGER NOT NULL,
    branch TEXT NOT NULL
    )""")

with sq.connect('Insurance_Company.db') as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO contract VALUES (?, ?, ?, ?, ?)", info)

with sq.connect('Insurance_Company.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM contract WHERE insurance_sum > 400000")
    result = cur.fetchall()
    print('Запрос №1',result, '\n')

with sq.connect('Insurance_Company.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM contract WHERE insurance_type = 'НС'")
    result = cur.fetchall()
    print('Запрос №2',result, '\n')

with sq.connect('Insurance_Company.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM contract WHERE tariff_rate BETWEEN 1000 AND 2500")
    result = cur.fetchall()
    print('Запрос №3',result, '\n')

with sq.connect('Insurance_Company.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE contract SET insurance_sum = insurance_sum + 15000 WHERE branch = '№1'")

with sq.connect('Insurance_Company.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM contract")
    print('Запрос №4', '\n')
    for result in cur:
        print(result)
    print('\n')

with sq.connect('Insurance_Company.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE contract SET tariff_rate = 20000 WHERE insurance_type = 'ОСАГО'")

with sq.connect('Insurance_Company.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM contract")
    print('Запрос №5', '\n')
    for result in cur:
        print(result)
    print('\n')

with sq.connect('Insurance_Company.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE contract SET insurance_sum = 150 WHERE insurance_type LIKE 'ДМС'")

with sq.connect('Insurance_Company.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM contract")
    print('Запрос №6', '\n')
    for result in cur:
        print(result)
    print('\n')

with sq.connect('Insurance_Company.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM contract WHERE insurance_type = 'ОСАГОS'")

with sq.connect('Insurance_Company.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM contract")
    print('Запрос №7','\n')
    for result in cur:
        print(result)
    print('\n')

with sq.connect('Insurance_Company.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM contract WHERE branch = '№3'")

with sq.connect('Insurance_Company.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM contract")
    print('Запрос №8','\n')
    for result in cur:
        print(result)
    print('\n')

with sq.connect('Insurance_Company.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM contract WHERE tariff_rate > 3000")

with sq.connect('Insurance_Company.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM contract")
    print('Запрос №9','\n')
    for result in cur:
        print(result)
    print('\n')