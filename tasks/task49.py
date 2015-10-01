"""The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?"""
from helpers.math_helper import generate_primes


def solve():
    limit = 10000
    primes = set(generate_primes(limit))

    return next(int(''.join(map(str, [a, b, c(a, b)])))
                for a in primes.intersection(range(1001, limit, 2))
                for b in primes.intersection(range(a + 2, limit, 2))
                if a != 1487
                if c(a, b) in primes
                if sorted(str(a)) == sorted(str(b)) == sorted(str(c(a, b))))


def c(a, b):
    return b + (b - a)


if __name__ == '__main__':
    print(solve())
