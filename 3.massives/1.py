# 1. Адекватное удаление итемов из списка (которые не пропускают элементы)
#list_1 = [1,2,3,4]

#for i , item in enumerate(list_1[:]):
#    list_1.remove(item)

#print(list_1)

# Крестики-нолика, где Х побеждает с первой попытки
#row = [''] * 3
#board = [row]*3

#board = [['']*3 for _ in range(len(row))]
#board[0][0] = 'X'
#print(board)


# 4. Игла в стоке сена

#t = ('one','two')
#for i in t:
#    print(i)
#c = ('one',)
#for i in c:
#    print(i)


# 5. Сохранить только уникальне значения
#list_1 = [1,3,4,6,6,4,3,3,5,6]
#list_1 = list(set(list_1))
#print(list(set(list_1)))


# 6. Ключи словаря - изменяемый объект
set_x = {1,2,3}
list_x = [1,4,7]
# Мы не можем в кач-ве ключа словарю передавать изменяемые объекты
# В данном случае нам нужно представить что-то из исходных в кач-ве неизменяемых
# К примеру List предствить как tuple, а множество как frozenset
dict_x = {frozenset(set_x):list_x}
dict_y = {tuple(list_x):set_x}
print(dict_x)
print(dict_y)