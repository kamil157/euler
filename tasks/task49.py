"""The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?"""
from helpers.math_helper import generate_primes


def task49():
    primes = set(generate_primes(10000))
    for a in range(1001, 10000, 2):
        if a in primes and a != 1487:
            for b in range(a + 2, 10000, 2):
                if b in primes:
                    c = b + (b - a)
                    if c in primes:
                        if sorted(str(a)) == sorted(str(b)) == sorted(str(c)):
                            return int(''.join(map(str, [a, b, c])))

if __name__ == '__main__':
    print(task49())
