# 1 2 3 4 5
# -> 2 -> fib(1) + fib(1)
# -> 3 -> fib(2) + fib(1)
# -> 4 -> fib(3) + fib(2)
# -> 5 -> fib(2) + fib(3)


def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    return fib(n - 1) + fib(n - 2)


for n in range(1, 9):
    print(n, "->", fib(n))
