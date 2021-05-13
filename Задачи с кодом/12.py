"""
Создайте функцию, которая принимает два параметра.
Eсли оба параметра — строки, то сложите их математически, если оба — integer, тогда сконкатенируйте их. Если параметры разного типа — верните None.
"""

def func(par1,par2):
    if type(par1) == type(par2):
        if type(par1) == int:
            return str(par1) + str(par2)
        return int(par1) + int(par2)
    else:
        return None

print(func('1','4'))