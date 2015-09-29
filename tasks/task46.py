"""It was proposed by Christian Goldbach that every odd composite number can
be written as the sum of a prime and twice a square.

9 = 7 + 2*1^2
15 = 7 + 2*2^2
21 = 3 + 2*3^2
25 = 7 + 2*3^2
27 = 19 + 2*2^2
33 = 31 + 2*1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum
of a prime and twice a square?"""
from itertools import count

from helpers.math_helper import is_prime


def task46():
    return next(n for n in count(3, 2)
                if not is_prime(n)
                if not is_goldbach(n))


def is_goldbach(n):
    return any(is_prime(n - 2 * i ** 2) for i in range(1, int(n ** 0.5)))


if __name__ == '__main__':
    print(task46())
