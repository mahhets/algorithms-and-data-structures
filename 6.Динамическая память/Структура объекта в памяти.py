"""
Значение переменной лежит отдельно в памяти, а переменная содержит в себе ссылку на конкретный объект памяти

Объект состоит из 3х компонентов:
    1. Счетчик ссылок
    2. Указатель на тип
    3. Содержимое
"""

import sys

a = 5
b = 123.5
c = 'Hellow'

# Адрес в памяти, по которому лежит объект целого типа
print(id(a))

# Модуль ctypes позволяет проанализировать данный объект
# Модуль struct позволяет расшифровать бинарную строку
# Исользуем метод string_at
import ctypes
import struct

print(ctypes.string_at(id(a), sys.getsizeof(a)))
# Расшифруем структуру на C для значений питон при помощи struct.unpack
print(struct.unpack('LLl', ctypes.string_at(id(a), 24)))
# Первое число - счетчик ссылок, второе - указатель на тип объекта, последнее - значение объекта