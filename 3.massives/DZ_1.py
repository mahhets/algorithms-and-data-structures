"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9
"""

ans = {}
for i in range(2,10):
    counter = 0
    for j in range(2,100):
        if j % i == 0:
            counter +=1
        ans[i] = counter

print(ans)
