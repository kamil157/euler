"""The number, 1406357289, is a 0 to 9 pandigital number because it is made
up of each of the digits 0 to 9 in some order, but it also has a rather
interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property."""
from itertools import permutations

from helpers.math_helper import generate_primes


def pandigitals():
    primes = list(generate_primes(17))
    return (int(''.join(pandigital))
            for pandigital in permutations('0123456789')
            # d2d3d4 is divisible by 2 iff d4 is divisible by 2
            if int(pandigital[3]) % 2 == 0
            # d4d5d6 is divisible by 5 iff d6 is divisible by 5 (= 0 or 5)
            # d6d7d8 is divisible by 11 -> d6 can't be 0 (011, 022, ...)
            if int(pandigital[5]) == 5
            if are_digits_divisible(pandigital, primes))


def are_digits_divisible(perm, primes):
    return all(int(''.join(perm[i + 1:i + 4])) % primes[i] == 0
               for i in range(7))


def task43():
    return sum(pandigitals())


if __name__ == '__main__':
    print(task43())
