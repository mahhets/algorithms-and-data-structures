"""
Во втором массиве сохранить индексы четных элементов первого массива
"""

tmp_1 = [1,2,3,4,5,6,7,8,9]
tmp_2 = []
for i, val in enumerate(tmp_1):
    if val % 2 == 0:
        tmp_2.append(i)

print(tmp_2)