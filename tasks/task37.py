"""The number 3797 has an interesting property. Being prime itself,
it is possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right
to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes."""

from helpers.math_helper import generate_primes

primes = set(generate_primes(1000000))


def truncatables():
    for n in primes:
        if n > 10:
            is_truncatable = True
            for i in range(1, len(str(n))):
                left = int(str(n)[:i])
                right = int(str(n)[i:])
                if left not in primes or right not in primes:
                    is_truncatable = False
            if is_truncatable:
                yield n


print(sum(truncatables()))