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
    insurance_summa INTEGER NOT NULL,
    insurance_type TEXT NOT NULL,
    tariff_rate INTEGER NOT NULL,
    branch TEXT NOT NULL
    )""")

with sq.connect('Insurance_Company.db') as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO contract VALUES (?, ?, ?, ?, ?)", info)
    result = cur.fetchall()
    print(result)
