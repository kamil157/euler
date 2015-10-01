"""The number 3797 has an interesting property. Being prime itself,
it is possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right
to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes."""

from helpers.math_helper import generate_primes


def truncatables():
    primes = set(generate_primes(1000000))
    return (n for n in primes
            if n > 10
            if is_truncatable(n, primes))


def is_truncatable(n, primes):
    s = str(n)
    return all(int(s[:i]) in primes and int(s[i:]) in primes
               for i in range(1, len(s)))


def solve():
    return sum(truncatables())


if __name__ == '__main__':
    print(solve())
