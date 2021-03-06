"""
Counter - подкласс словаря
Неупорядоченная коллекция пар "ключ - значение"
Где значение - частота вхождения ключа
"""

from collections import Counter

# пустая коллекция
a = Counter()

# коллекция, основанная на строке
b = Counter('assddvs')

# коллекция, основанная на словаре
c = Counter({'red':2,'blue':4})

# коллекция, основанная на ключевых аргументах
d = Counter(cats=4, dogs =5)

print(a, b, c, d, sep='\n')

print(b['z'])

b['z'] = 0
print(b)

# elemenst - возвращает набор итерируемых объектов
# выведет только те объекты, у которх значение положительное число
print('*'*30)
print(list(b.elements()))

# most_common - список, элементами которого являются кортежи + фильтрация по частоте встречь
print('*'*30)
print(b.most_common(2))

# subtract - вычитать из одной коллекции другую
print('*'*30)
a = Counter(t = 1, r = -5, y = 4)
b = Counter(t = 4, r = -2, y = -2)
a.subtract(b)
print(a)

# clear - удаляет все элементы из Counter
print('*'*30)
a.clear()
print(a)

# Приведение к другим типам
print('*'*30)
print(set(b))
print(dict(b))

# Логические операции
a = Counter(a = 5, b = 3)
b = Counter(a = 4, b = 5)
print('*'*30)
print(a + b)
print(a - b)
print(a & b) # вернет кол-во значений, которое есть и в 1 и во 2 случаях
print(a | b) # или вернет максимальные значения

# Унарные элементы
z = Counter(a = -2, b = 5)
print('*'*30)
print(+z) # вернет только положительные элементы
print(-z) # вернет только отрицательные, при этом меняя знак