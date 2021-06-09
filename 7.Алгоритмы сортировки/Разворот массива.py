"""
Разворот массива
"""

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)

def revers(array):
    for i in range(len(array) // 2):
        array[i], array[len(array) -i - 1] = array[len(array) - i - 1], array[i]


revers(array)
print(array)

"""
Встроенная сортировка в Python позволяет отсортировать по порядку возростания .sort()
sort может принимать аргумент reverse = True, который выполнит разворот массива
"""
print('*'*50)
t = tuple(random.randint(0,100) for _ in range(10))
print(t)

"""
Кортежи неизменяемы, но для их сортировки тоже есть встроенная функция - sorted, которая тоже принимает reverse
"""
print('*'*50)
t = tuple(sorted(t))
print(t)

