"""

"""

import sys

print(sys.version, sys.platform) # Версия python, OS

a = 5
b = 123.5
c = 'Hellow'

# Чтобы узнать, сколько памяти занимают объекты байтах
# sys.getsizeof()
print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))

# Список
lst = [i for i in range(10)]
print(sys.getsizeof(lst))
# получилось 192 байта, значит среди этих 192 байт есть 10 байт, которые содержат ссылки


def show_size(x, level = 0):
    """
    Напишем функцию, которая будет показывать сколько занимают объекты и их части
    :param x:
    :param level:
    :return:
    """
    print('\t'*level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')

    if hasattr(x,'__iter__'):
        if hasattr(x,'items'):
            for xx in x.items():
                show_size(xx, level+1)
        elif not isinstance(x,str):
            for xx in x:
                show_size(xx,level + 1)

# Список
show_size(lst)

# Кортеж
print('*'*40)
t = tuple(lst)
show_size(t)

# Множество
print('*'*40)
s = set(lst)
show_size(s)

# Словарь
print('*'*40)
d = {str(i):i for i in range(10)}
show_size(d)


