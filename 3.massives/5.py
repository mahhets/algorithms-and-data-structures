# Ассоциативный массив, словарь (ключ - значение других столбцов, как в SQL)

"""
Пользователь вводит кол-во предприятий, названия, плановую и фактическую прибыль каждого предприятия
Вычислить процент выполнения плана и вывести данные с предварительной фильтрацией
"""

k = int(input('Введите кол-во предприятий: '))
enterprises = {}

for i in range(1, k+1):
    name = input('Название предприятия: ')
    enterprises[name] = [float(input('Введите плановую прибыль:')),
                         float(input('Введите фактическую прибыль: '))]
    enterprises[name].append(enterprises[name][1]/enterprises[name][0])
for i,item in enterprises.items():
    if item[1] > 0:
        print(f'Предприятие {i} заработало {item[1]} что составило {item[2] * 100:.2f}%')
