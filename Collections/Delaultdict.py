"""
Defaultdict - подкласс словаря
При создании объекта передаем функцию
"""

from collections import defaultdict

a = defaultdict()
print(a)

# Подсчет кол-ва элементов
s = 'sdgaramacvmakgdfknv'
b = defaultdict(int)
for i in s:
    b[i] +=1

print(b)

# У нас есть 3 датчика, которые передают сигналы о своем статусе
# Нужно понять каки сигналы какой передавал
print('*'*40)
list_1 = [('cat', 1), ('dog', 5),('cat', 2),('mouse',1),('dog', 1)]
c = defaultdict(list)
for k, v in list_1:
    c[k].append(v)

print(c)

# Оставить только уникальные сигнлы от каждого датчика
print('*'*40)
list_2 = [('cat', 1), ('dog', 5),('cat', 2),('mouse',1),('dog', 1),('dog',5)]
d = defaultdict(set)
for k, v in list_2:
    d[k].add(v)

print(d)


# Пример с lambda функцией
print('*'*40)
f = defaultdict(lambda: 'unknown')
f.update(rex = 'dog', tomas = 'cat')
print(f['rex'])
print(f['jerry'])