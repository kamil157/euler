"""We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?"""
from itertools import permutations


def is_prime(n):
    if n % 2 == 0 and n > 2 or n < 2:
        return False
    return all(n % i for i in range(3, int(n ** 0.5) + 1, 2))


def pandigitals():
    for length in range(1, 8):
        digits = ''.join([str(i) for i in range(1, length + 1)])
        for perm in permutations(str(digits)):
            n = int(''.join(perm))
            if is_prime(n):
                yield n


print(max(pandigitals()))