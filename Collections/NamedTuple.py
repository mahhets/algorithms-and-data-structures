"""
Именованный кортеж, обеспечивающий доступ к данным по номерам
"""

from collections import namedtuple

hero_1 = {'Aaz','Izverg',100,0.0,250}

class Person:
    def __init__(self, name, race, health, mana, strenght):
        self.name = name
        self.race = race
        self.healh = health
        self.mana = mana
        self.strenght = strenght

"""
Вместо создания класса можно воспользоваться именованным кортежем
"""

New_person = namedtuple('New_person','name , race, health, mana, strenght')
hero_2 = New_person('Aaz','Izverg',100,50,250)
print(hero_2.race)

# Также можно в кач-ве ключей передавать массив с ключами
# Существует опасность передачи нежелательных значений
# С этим можно бороться посредством передачи параметра rename=True после передачи списка
# New_person_2 = namedtuple('New_person_2', list_1, rename=True)

list_1 = ['name','race','heatlh','mana','strenght']
New_person_2 = namedtuple('New_person_2', list_1)
hero_3 = New_person_2('Mahh','Human',100,100,50)
print(hero_3.name)

# _make() - передать и одновременно создать объект в namedtuple
Point = namedtuple('Point','x,y,z')
t = [1,5,3]
p2 =Point._make(t)
print(p2)

# _asdict() - преобразует namedtuple в ordereddict

# _replace() - заменить(переписать) значения

# _fields - показать поля namedtuple

# Задать значения по умолчанию defaulst = []
# Point = namedtuple('Point','x,y,z', defaults = [0,0])