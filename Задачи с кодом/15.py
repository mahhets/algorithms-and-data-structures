"""
Даны параметры: день, месяц и год.
Напишите функцию, которая определяет, существует ли такая дата или нет. Используйте модуль datetime.
"""

import datetime

def func(day,month,year):
    try:
        date = datetime.date(year,month,day)
    except: return False
    return True

print(func(12,14,51))