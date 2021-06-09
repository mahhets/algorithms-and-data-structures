"""
Сортировка сложных структур с использование ключа
"""

from collections import namedtuple

Person = namedtuple('Pesron', 'name, age')

p_1 = Person('Васян', 25)
p_2 = Person('Олег', 20)
p_3 = Person('Лена', 30)


guys = [p_1,p_2,p_3]
print(guys)

"""
1. Отсортируем по имени(алфавиту)
2. Отсортируем по возрасту
"""
print('*'*50)
res_1 = sorted(guys)
print(res_1)

def by_age(person):
    return person.age

res_2 = sorted(guys, key=by_age)
print(res_2)

"""
Но можно и не писать функцию, достаточно ипортировать attrgetter и через него в key передать возраст
"""
from operator import attrgetter

res_2 = sorted(guys,key=attrgetter('age'))
print(res_2)
