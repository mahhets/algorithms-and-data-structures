"""
В log файл сервер добавляет ip-адрема, с которых пришел запрос
Проанализировать последие N адресов и сохранить в новый файл пары значений
"ip - кол-во запросов"

!!! Исключить локальные ip-адреса
!!! Сохранить исходный порядок
"""

from collections import OrderedDict, defaultdict, deque

N = 3000
with open('big_log.txt', 'r', encoding='utf-8') as f:
    log = deque(f, N)

data =OrderedDict()
spam = defaultdict(int)

for item in log:
    ip = item[:-1]
    if not ip.startswith('192.168'):
        spam[ip] +=1
        data[ip] = 1

data.update(spam)
with open('data.txt','w',encoding='utf-8') as f:
    for key, value in data.items():
        f.write(f'{key}  -  {value}\n')