"""The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct prime factors.
What is the first of these numbers?"""
from tasks.task12 import divisors
from helpers.math_helper import generate_primes, divisors

primes = set(generate_primes(1000))

for start in range(1000000):
    ok = True
    for i in range(start, start + 4):
        factors = divisors(i)
        prime_factors = factors.intersection(primes) - {1}
        if len(prime_factors) != 4:
            ok = False
    if ok:
        print(start)
        exit()
