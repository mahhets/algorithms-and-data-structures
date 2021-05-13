"""
Выведите список файлов в указанной директории.
"""

from os import listdir
from os.path import isfile, join
files = [f for f in listdir('C:/') if isfile(join('C:/', f))]
print(files)