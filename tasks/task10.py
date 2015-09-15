"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""
from helpers.math_helper import generate_primes


def task10():
    return sum(generate_primes(2000000))


if __name__ == '__main__':
    print(task10())
