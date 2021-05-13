"""
ChainMap - цепочка из словарей
Поиск ключа осуществляется последовательно в каждом из словарей цепочки, пока ключ не будет найдет
"""

from collections import ChainMap

dict_1 = {'a':2,'b':4,'c':6}
dict_2 = {'a':10,'b':12,'d':15}

d_map = ChainMap(dict_1, dict_2)

print(d_map)

# Ссылочная структура данных
dict_2['a'] = 100
print(d_map)

# Поиск по ключу
print('*'*40)
print(d_map['a'])
print(d_map['d'])

# new_child() - взять существующую коллекцию и добавить новый словарь в начало
print('*'*40)
x = d_map.new_child()
print(x)

# maps() - позволяет обратиться непосредственно к одному из словарей
print('*'*40)
print(x.maps[1]['b'])
print(x.maps[-1])

# parents - вывести родительский словарь или словари, которые были изначально при создании ChainMap
print(x.parents)