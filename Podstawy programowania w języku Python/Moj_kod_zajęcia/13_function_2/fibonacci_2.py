# 1 1 2 3 5 -> 5 ->
# fib(5) = fib(2) + fib(3)
# fib(3) = 1 + 1

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    return fib(n - 1) + fib(n - 2)


for n in range(1, 17):
    print(n, "->", fib(n))
