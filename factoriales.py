def factorial(n):
    """
    Calculate the factoial of n
    n int > 0
    return n!
    """
    print(n)
    if n == 1:
        return 1
    return n * factorial(n - 1)


n = int(input('Escribe un entero: '))

print(factorial(n))
