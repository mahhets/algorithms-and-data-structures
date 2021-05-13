"""
Напишите функцию, которая преобразовывает dict в список списков.
Возвращаем пустой список, если словарь пустой.
"""

def func(dct):
    if len(dct) > 0:
        return [[key,value] for key,value in dct.items()]


dc = {5:67,4:10,1:4}

print(func(dc))