"""We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?"""
from itertools import permutations

from helpers.math_helper import is_prime


def pandigitals():
    for length in range(1, 8):
        digits = ''.join([str(i) for i in range(1, length + 1)])
        for perm in permutations(str(digits)):
            n = int(''.join(perm))
            if is_prime(n):
                yield n


def task41():
    return max(pandigitals())


if __name__ == '__main__':
    print(task41())
