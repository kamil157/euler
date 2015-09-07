"""The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?"""
from helpers.math_helper import generate_primes


def task50():
    return max(consecutive_primes())[1]


def consecutive_primes():
    limit = 1000000
    primes_list = list(generate_primes(limit))
    primes_set = set(primes_list)
    for i in range(10):
        prime_sum = 0
        for j in range(i, len(primes_list)):
            prime_sum += primes_list[j]
            if prime_sum in primes_set:
                yield j - i + 1, prime_sum


if __name__ == '__main__':
    print(task50())
