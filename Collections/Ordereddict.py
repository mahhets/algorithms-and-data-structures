"""
Ordereddict - подкласс словаря, в котором элементы("ключ - значение") упорядоченны
Запоминает порядок, в котором были добавлены ключи
"""

from collections import OrderedDict

# Сортировка по алфaвиту
a = {'cat':5, 'dog':2, 'mouse':4}
b = OrderedDict(sorted(a.items(), key=lambda x: x[0]))
print(b)

# Сортировка по значению
print('*'*40)
с = OrderedDict(sorted(a.items(), key=lambda x: x[1]))
print(с)

# Поместить объект в конец словаря
# move_to_end(last=True/False)
# move_to_end(last=False) - переместит в начало
print('*'*40)
b.move_to_end('mouse')
print(b)
b.move_to_end('mouse',last=False)
print(b)


# popitem - удаление последнего / первого элемента
print('*'*40)
b.popitem() # last = False
print(b)


# Возможность сортировка по другой характеристике
# Отсортируем список по длине ключа
print('*'*40)
new_a = OrderedDict(sorted(a.items(), key=lambda x: len(x[0])))
print(new_a)








