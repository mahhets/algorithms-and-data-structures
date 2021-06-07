"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
"""
import random
tmp = [random.randint(-10,10) for _ in range(20)]
print(tmp)
min_idx_1, min_idx_2 = None,None
min_el_1, min_el_2 = 0, 0
for idx, value in enumerate(tmp):
    if value < min_el_1:
        min_idx_1 = idx
        min_el_1 = value
    if value < min_el_2 and idx != min_idx_1:
        min_el_2 = value
        min_idx_2 = idx

print((min_idx_1, min_idx_2),(min_el_1, min_el_2))