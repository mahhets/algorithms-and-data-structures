# Двоичный(бинарный) поиск элементов в массиве для упорядоченных массивов

temp = [1,3,7,8,13,16,19,20,25,34,46]

def binary_search(array, value):
    # задаем начальные значения. left - первый элемент массива, right - последний
    left = 0
    right = len(array) - 1
    pos = len(array) // 2
    while array[pos] != value and left <= right:
        if value > array[pos]:
            left = pos + 1
        else:
            right = pos - 1

        pos = (left + right) // 2

    return print('Элемента нет в массиве') if left > right else pos

binary_search(temp, 21)