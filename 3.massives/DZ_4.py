"""
Определить, какое число в массиве встречается чаще всего
"""
import random

tmp = [random.randint(-10,10) for _ in range(40)]
subtmp = set(tmp)
counter = {}
for el in subtmp:
    countel = 0
    for val in tmp:
        if el == val:
            countel +=1
    counter[el] = countel

print(counter)

equal = 0
fin_idx = 0
for i in counter:
    if counter[i] > equal:
        equal = counter[i]
        fin_idx = i

print(fin_idx, counter[fin_idx])
    