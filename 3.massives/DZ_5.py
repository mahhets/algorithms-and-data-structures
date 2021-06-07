"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
"""

import random

tmp = [random.randint(-10,10) for _ in range(20)]
print(tmp)
idx, value = 0, tmp[0]
for i, j in enumerate(tmp):
    if j < value:
        idx, value = i, j
print((idx, value))
