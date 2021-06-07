import random


matrix = [[random.randint(1,50) for _ in range(5)] for _ in range(5)]
for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()

### Посчитать сумму строк и столбцов матрицы

#sum_column = [0] *len(matrix[0])
#for line in matrix:
#    sum_line = 0
#    for i, item in enumerate(line):
#        sum_line +=item
#        sum_column[i] +=item

#        print(f'{item:>4}', end='')
#    print(f'    | {sum_line}')
#print('-'*30)
#for i in sum_column: print(f'{i:>4}', end='')