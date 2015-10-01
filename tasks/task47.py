"""The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct prime factors.
What is the first of these numbers?"""
from itertools import count

from helpers.math_helper import generate_primes, divisors


def solve():
    primes = set(generate_primes(1000))
    return next(n for n in count() if has_four_factors(primes, n))


def has_four_factors(primes, n):
    return all(prime_factors(i, primes) == 4 for i in range(n, n + 4))


def prime_factors(i, primes):
    return len(divisors(i).intersection(primes))


if __name__ == '__main__':
    print(solve())
