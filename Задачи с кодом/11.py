"""
Напишите функцию, которая рекурсивно вернет количество гласных в строке.
"""

def func(text):
    return 0 if not text else (text[0] in 'aeiouAEIOU') + func(text[1:])

l = 'lalava'
l2 = 'tttaplrx'

print(func(l2))