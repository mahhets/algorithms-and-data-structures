"""
Требуется написать программу, которая будет запускаться из скрипта и принимать параметры ip и port
"""

import argparse
from collections import ChainMap

defaults = {'ip':'localhost','port':8888}

parser = argparse.ArgumentParser()
parser.add_argument('-i','--ip')
parser.add_argument('-p','--port')

args = parser.parse_args()
# благодаря функции vars мы сохраним ключи в key, а значения в value
new_dict = {key: value for key,value in vars(args).items() if value}

settings = ChainMap(new_dict,defaults)
print(settings['ip'])
print(settings['port'])