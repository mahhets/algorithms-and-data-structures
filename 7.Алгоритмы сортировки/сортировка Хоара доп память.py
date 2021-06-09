"""
Сортировка Хоара (одна из самых быстрых)

Сложност: в худшем - O(n**2), в лучшем - O(n logn)
Устойчивость: Неустойчивая
Тип: Обменная
Потребление памяти: O(n)
"""

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)
"""
1. Выбираем опорный элемент (любой)
2. Сравниваем все элементы с опорным и расставляем в массиве так, чтобы рабить их
    на 3 непрерывных отрезка:
        1. Меньше опорного
        2. Равные опорному
        3. Больше опорного
3. Для отрезком меньше и больше рекурсивно выполняем сортировку
"""


# Версия с дополнительной памятью
def quick_sort(array):

    if len(array) <=1:
        return array

    pivot = random.choice(array)
    s_ar, m_ar, l_ar = [], [], []

    for item in array:
        if item < pivot:
            s_ar.append(item)
        elif item == pivot:
            m_ar.append(item)
        elif item > pivot:
            l_ar.append(item)
        else:
            raise Exception('Случилось ужасное')

    return quick_sort(s_ar) + m_ar + quick_sort(l_ar)

array_new = quick_sort(array)
print(array_new)



