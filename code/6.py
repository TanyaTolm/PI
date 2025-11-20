def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fib_num = list(fib(200))

print('200-е число Фибоначи равно: ', fib_num[-1])