"""
Оптимизаия кода при прмрщи мемоизации
Мемоизация - сохранение результатов выполнения функции для предотвращения повторных вычислений
"""
import cProfile

def test_fib(func):
    tmp = [0,1,1,2,3,5,8,13,21,34]
    for i, item in enumerate(tmp):
        assert item == func(i)
        print(f'Test {i} OK')


def fib_dict(n):
    fib_d= {0:0,1:1}
    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]

        fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
        return fib_d[n]

    return _fib_dict(n)

def fib_list(n):
    fib_d= [None] * 1000
    fib_d[:2] = [0,1]
    def _fib_list(n):
        if fib_d[n] is None:
            fib_d[n] = _fib_list(n - 1) + _fib_list(n - 2)
        return fib_d[n]

    return _fib_list(n)

# test_fib(fib_list)

# 100 loops, best of 5: 20.1 usec per loop


# cProfile
#

cProfile.run('fib_list(40)')