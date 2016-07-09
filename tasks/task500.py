"""
The number of divisors of 120 is 16.
In fact 120 is the smallest number having 16 divisors.

Find the smallest number with 2^500500 divisors.
Give your answer modulo 500500507."""
from heapq import heappop, heappush

from helpers import math_helper


def solve():
    primes = math_helper.generate_primes(7500000)
    heap = []
    for value in primes:
        heappush(heap, value)

    n = 1
    for power in range(500500):
        head = heappop(heap)
        n *= head
        n %= 500500507
        heappush(heap, head ** 2)

    return n


if __name__ == '__main__':
    print(solve())
