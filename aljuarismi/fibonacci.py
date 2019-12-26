def fib(n):
    """Calcula la sucesion de Fibonacci y la imprime una a una."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b

def fib_list(n):
    """Calcula la sucesion de Fibonacci y la retorna en una lista."""
    a,b = 0, 1
    sequence = []
    while a < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(fib.__doc__)
print(fib(2000))
print(fib_list.__doc__)
print(fib_list(2000))