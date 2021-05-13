"""
Создайте функцию, которая вернет индексы всех вхождений элемента в списке.
"""

def func(lst,elem):
    return [i for i in range(len(lst)) if lst[i] == elem]

l = [1,2,5,7,8,5,4,3,4,5,8,7,6,7,8,9]

print(func(l,8))