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


# TODO slow
def divisors(n):
    factors = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return factors


def spiral(n):
    k = 1
    yield k

    for i in range(1, n + 1):
        for _ in range(4):
            k += 2 * i
            yield k


def is_prime(n):
    if n % 2 == 0 and n > 2 or n < 2:
        return False
    return all(n % i for i in range(3, int(n ** 0.5) + 1, 2))


def partitions(coins, target):
    a = [0] * (target + 1)
    a[0] = 1
    for coin in coins:
        for i in range(coin, target + 1):
            a[i] += a[i - coin]
    return a[target]