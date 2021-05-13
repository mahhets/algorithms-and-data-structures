"""
Deque - очередь.
Объект, в котором одержится список элементов(итерируемый)
"""

from collections import deque

a = deque()
b = deque('afhthr')
c = deque([1,2,3,4,5])
print(a,b,c,sep='\n')

"""
При формировании очереди мы можем задать максимальную длину очереди
maxlen = num
Если длина не может вмстить в себя все элементы, то при добовлении еще однго элемента
в конец очереди, первый элемент выпадает
"""

b = deque([1,2,3,4,5], maxlen=4)
c = deque('abcde', maxlen=3)
print('*'*30)
print(b, c, sep='\n')


# clear() - очистит очередь

# Добавление элементов - append / appendleft
print('*'*40)
b = deque([i for i in range(5)], maxlen=7)
b.append(6) # добавить элемент в конец очереди
print(b)
b.appendleft(7) # добавить элемент в начало очереди
print(b)
b.extend([10,11,12]) # добавление списка в спиок/очередь
b.extendleft([20,21,22])
print(b)

# Забираем элементы - pop / popleft
f = deque([i for i in range(6)], maxlen=7)
x = f.pop()
y = f.popleft()
print(f, x, y, sep='\n')

print('*'*40)
f = deque([i for i in range(6)], maxlen=7)
print(f.count(2)) # сколько раз элемент входит в очередь
print(f.index(4)) # под каким индексом находится элемент
f.insert(2,6) # вставить 6 на позицию 2
print(f)

print('*'*40)
f.reverse() # развернуть очередь
print(f)
f.rotate(-3) # переведет часть элементов из правой в левую или из левой в правую(отрицательное n)
print(f)