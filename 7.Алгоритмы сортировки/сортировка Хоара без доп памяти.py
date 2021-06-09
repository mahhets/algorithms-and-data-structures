"""
Сортировка Хоара (одна из самых быстрых)

Сложност: в худшем - O(n**2), в лучшем - O(n logn)
Устойчивость: Неустойчивая
Тип: Обменная
Потребление памяти: Не требует доп.памяти
"""

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)

def quick_sort(array, fst, lst):

    if fst >= lst:
        return

    pivot = array[random.randint(fst,lst)]
    i, j = fst, lst # нужны чтобы отслеживать индексы, позволят менять местами элементы относительно опорного

    while i <= j:
        while array[i] < pivot:
            i +=1

        while array[j] > pivot:
            j -=1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1

    quick_sort(array, fst, j)
    quick_sort(array, i, lst)


quick_sort(array,0,len(array) - 1)
print(array)