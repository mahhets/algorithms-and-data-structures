"""
Напишите программу, которая принимает имя файла и выводит его расширение.
Если расширение у файла определить невозможно, выбросите исключение.
"""

def filename(file):
    filename_parts = file.split('.')
    if len(filename_parts) < 2:
        raise ValueError('У файла нет расширения')
    first, *middle, last = filename_parts
    if not last or not first and not middle:
        raise ValueError('У файла нет расширения')
    return filename_parts[-1]

text = 'lalal.py'

print(filename(text))