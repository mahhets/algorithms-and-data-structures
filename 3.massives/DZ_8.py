"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
"""
print('Введите через пробел элементы матрицы 4х4')
tmp = [[input(f'Введите элементы {i+1} строки: ') for _ in range(1)] for i in range(4)]
matrix = []
for line in tmp:
    for el in line:
        elements = [int(i) for i in el.split(' ')]
        matrix.append(elements)

for line in matrix:
    line_sum = 0
    for item in line:
        line_sum +=item
        print(f'{item:>4}', end='')
    print(f'{line_sum:>4}')

