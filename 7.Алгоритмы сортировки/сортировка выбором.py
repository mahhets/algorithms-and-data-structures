"""
Алгоритм сортировки выбором
Сложность: O(n**2)
Устойчивость: Устойчивая
Тип: Выбором
Потребление памяти: Не требует доп.памяти
"""

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)

"""
1. Найти наименьший элемент в неотсортированном массиве
2. Меняем его местами с первым элементов в неотсортированной части массива
После этого действия первая ячейка массива считается отсортированной
3. Продолжать пункты 1-2 пока весь массив не будет отсортирован
"""

def selection_sort(array):
    for i in range(len(array)):
        idx_min = i

        for j in range(i + 1, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j

        array[idx_min], array[i] = array[i], array[idx_min]



