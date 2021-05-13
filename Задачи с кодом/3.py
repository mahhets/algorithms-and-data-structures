"""
Дан список. Нужно написать функцию, которая будет удалять все элементы списка до определенного.
"""

def cleaner_n(lst,n):
    try:
        return lst[lst.index(n):]
    except ValueError:
        return lst


l = [8,4,5,6,8,2,3,5]

print(cleaner_n(l,6))
