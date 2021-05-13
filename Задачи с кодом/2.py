"""
Разделить строку на пары символов.
Если строка состоит из нечетного количества символов,
то недостающий символ в результирующем списке пар заменяется на знак нижнего подчеркивания _ .
"""


def split_pairs(line):
    n = 2
    pairs = []
    for i in range(0,len(line),n):
        element = line[i:i+n]
        if len(element) == 1:
            pairs.append(element+'_')
        else:
            pairs.append(element)
    return pairs

text = 'dahdhbbdbdfdv'

print(split_pairs(text))