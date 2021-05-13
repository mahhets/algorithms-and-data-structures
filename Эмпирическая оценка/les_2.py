import cProfile

def test_fib(func):
    tmp = [0,1,1,2,3,5,8,13,21,34]
    for i, item in enumerate(tmp):
        assert item == func(i)
        print(f'Test {i} OK')


def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


# 10
# 100 loops, best of 5: 55.5 usec per loop

# 20
# 100 loops, best of 5: 8.57 msec per loop


# cProfile

cProfile.run('fib(40)')