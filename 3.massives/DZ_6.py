"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random
tmp = [random.randint(-30,30) for _ in range(20)]
print(tmp)
min_idx, max_idx = None, None
min_value, max_value = 0,0
for i, value in enumerate(tmp):
    if value < min_value:
        min_idx = i
        min_value = value
    elif value > max_value:
        max_idx = i
        max_value = value

counter = 0
if min_idx > max_idx:
    for value in tmp[max_idx+1:min_idx]:
        counter += value
else:
    for value in tmp[min_idx+1:max_idx]:
        counter += value
print(min_idx, max_idx)
print(counter)