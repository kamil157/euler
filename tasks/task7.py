"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?"""
from helpers.math_helper import generate_primes


def solve():
    return list(generate_primes(200000))[10000]


if __name__ == "__main__":
    print(solve())
