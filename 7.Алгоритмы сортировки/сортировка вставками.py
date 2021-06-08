"""
Алгоритм сортировки вставками

Сложность: O(n**2)/ лучшее время O(n)
Устойчивость: устойчивая
Тип: Вставками
Потребление памяти: не требует доп.памяти
"""

"""
0. В самом начале договариваемся, что первый элемент уже отсортирован
1. Из массива последовательно бретеся каждый элемент, кроме index == 0
2. Этот элемент вставляется в отсортированную часть массива
"""

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)

def insertion_sort(array):

    for i in range(1, len(array)):
        spam = array[i]
        j = i

        while array[j - 1] > spam and j > 0:
            array[j] = array[j - 1]
            j -=1

        array[j] = spam
        print(array)


insertion_sort(array)
print(array)