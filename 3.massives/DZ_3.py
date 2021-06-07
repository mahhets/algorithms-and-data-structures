"""
В массиве случайнх чисел поменять местами минимальный и максимальный элементы
"""
import random
tmp = [random.randint(-100,100) for _ in range(20)]

maxel = 0
max_idx = 0
minel = 0
min_idx = 0
for i, val in enumerate(tmp):
    if val > maxel:
        maxel, max_idx = val, i

    elif val < minel:
        minel, min_idx = val, i

print((maxel,max_idx),(minel, min_idx))
print(tmp)
tmp[max_idx], tmp[min_idx] = tmp[min_idx], tmp[max_idx]
print(tmp)

