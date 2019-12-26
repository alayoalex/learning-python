def factorial_recursivo(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

def factorial_recursivo_2(n):
    if n is (0,1):
        return 1
    return n * factorial(n - 1)

def factorial_iterativo(n):
    pass

print(factorial_recursivo(5))
print(factorial_recursivo_2(10))