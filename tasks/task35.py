"""The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?"""

from helpers.math_helper import generate_primes


def generate_circulars():
    for p in primes:
        s = str(p)
        is_circular = True
        for i in range(1, len(s)):
            rotated = int(s[i:] + s[:i])
            if rotated not in primes:
                is_circular = False
        if is_circular:
            yield p


primes = set(generate_primes(1000000))

print(len(list(generate_circulars())))