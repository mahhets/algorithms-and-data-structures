# Разложить положительные и отрицательные числа по разным массивам

#tmp = [1,3,5,-3,-2,4,-7,-4,7,0,3]
#array_below = []
#array_large = []
#for i in tmp:
#    if i >= 0:
#        array_below.append(i)
#    else:
#        array_large.append(i)
#print(array_below, array_large)


# Вставка элемента в произвольное место массива

tmp = [1,3,5,-3,-2,4,-7,-4,7,0,3]

def array_inputer(array, val, pos):
    array.append(None)
    i = len(array) - 1
    while i > pos:
        array[i], array[i-1] = array[i-1], array[i]
        i -= 1
    array[pos] = val
    return array

print(array_inputer(tmp,43,4))