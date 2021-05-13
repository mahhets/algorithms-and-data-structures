"""
Оптимизаия кода при прмрщи мемоизации
Мемоизация - сохранение результатов выполнения функции для предотвращения повторных вычислений
"""

import cProfile
import functools


def test_fib(func):
    tmp = [0,1,1,2,3,5,8,13,21,34]
    for i, item in enumerate(tmp):
        assert item == func(i)
        print(f'Test {i} OK')

# декоратор, который запоминает результаты выполнения функции

@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# 10
# 100 loops, best of 5: 247 nsec per loop


# 100
#