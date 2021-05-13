"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего.
"""

from collections import namedtuple

Company = namedtuple('Company','name, profit_1, profit_2, profit_3, profit_4')
comp_number = int(input('Введите кол-во предприятий: '))

high_avg = []
low_avg = []

company_list = [Company(
    input('Имя компании: '),
    float(input('Прибыль за 1 квартал: ')),
    float(input('Прибыль за 2 квартал: ')),
    float(input('Прибыль за 3 квартал: ')),
    float(input('Прибыль за 4 квартал: '))
) for _ in range(comp_number)]


def average_profit(company):
    prof_sum = company.profit_1 + company.profit_2 + company.profit_3 + company.profit_4
    return prof_sum / 4

all_avg = sum([average_profit(company_list[i]) for i in range(comp_number)]) / comp_number


for comp in company_list:
    if average_profit(comp) >= all_avg:
        high_avg.append(comp.name)
    else:
        low_avg.append(comp.name)

print('Выше среднего: ', high_avg)
print('Ниже среднего: ', low_avg)