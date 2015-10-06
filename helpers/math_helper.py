from ctypes import cdll
from functools import lru_cache, reduce
from operator import mul
import operator


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


def num_divisors(n):
    if "lib" not in num_divisors.__dict__:
        num_divisors.lib = cdll.LoadLibrary('..\lib\Euler++')
    return num_divisors.lib.numDivisors(n)


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


def prod(s):
    return reduce(mul, s, 1)


def resilience(n):
    return phi(n) / (n - 1)


def phi(n):
    return int(n * prod(1 - 1 / p for p in set(prime_factors(n))))


def read_grid(string):
    lines = string.split('\n')
    values = [line.split() for line in lines]
    return [[int(n) for n in line] for line in values]


def get_max_path(tree):
    for row in reversed(range(len(tree) - 1)):
        for col in range(row + 1):
            tree[row][col] += max(tree[row + 1][col], tree[row + 1][col + 1])
    return tree[0][0]


def proper_divisor_sum(n):
    return sum(divisors(n)) - n


def is_palindrome(s):
    return str(s) == str(s)[::-1]


def choose(n, r):
    if n < r:
        return 0
    r = min(r, n - r)
    if r == 0:
        return 1
    numer = reduce(operator.mul, range(n, n - r, -1))
    denom = reduce(operator.mul, range(1, r + 1))
    return numer // denom


def word_value(word):
    return sum(ord(c) - ord('A') + 1 for c in word.upper())


def pentagonal(limit):
    return (n * (3 * n - 1) // 2 for n in range(1, limit))


def hexagonal(limit):
    return (n * (2 * n - 1) for n in range(1, limit))
