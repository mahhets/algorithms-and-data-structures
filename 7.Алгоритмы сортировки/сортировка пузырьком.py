"""
Алгоритм сортировки пузырьком

Сложность: O(n**2)
Устойчивость: Устойчивая
Тип: Обменная
ПОтребление памяти: не требует дом.памяти
"""

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)

"""
1.Берем первый элемент и сравниваем со вторым. Если первый элемент окажется больше второго > меняем их местами
2.Таким образом проходимся по всему списку
3.Повторяем шаги 1-2
"""

n = 1
while n < len(array):
    for i in range(len(array) - n):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
    n +=1
print(array)