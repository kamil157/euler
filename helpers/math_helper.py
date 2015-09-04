from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def prime_factors(n):
    i = 2
    while n > 1:
        while n % i == 0:
            yield i
            n /= i
        i += 1


def generate_primes(limit):
    if limit < 2:
        return []
    a = [True] * (limit + 1)
    a[0] = a[1] = False

    for (i, is_prime) in enumerate(a):
        if is_prime:
            yield i
            for n in range(i * i, limit + 1, i):
                a[n] = False