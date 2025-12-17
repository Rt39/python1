def factorial(n):
    if n <= 2:
        return n
    else:
        return n * factorial(n - 1)

def fibonacci(n: int) -> int:
    """
    Compute the nth Fibonacci number.
    """
    return fib_helper(n)

def fib_helper(
        n: int,
        F_nm2: int = 0, F_nm1: int = 1
    ) -> int:
    """
    Helper function to compute the nth
    Fibonacci number using tail recursion.
    F_nm2: Fibonacci(n-2)
    F_nm1: Fibonacci(n-1)
    """
    if n == 0: return F_nm2
    elif n == 1: return F_nm1
    else: return fib_helper(
            n - 1, F_nm1, F_nm2 + F_nm1
        )

def mypow(x: int, n: int) -> int:
    if n == 0:
        return 1

    if n % 2 == 0:
        half_pow = mypow(x, n // 2)
        return half_pow * half_pow
    else:
        return x * mypow(x, n - 1)

def reverse(lst: list) -> list:
    if len(lst) <= 1:
        return lst
    return reverse(lst[1:]) + [lst[0]]

def catalan(n: int) -> int:
    if n <= 1:
        return 1
    res = 0
    for i in range(n):
        res += catalan(i) * catalan(n - i - 1)
    return res