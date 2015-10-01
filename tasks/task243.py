"""A positive fraction whose numerator is less than its denominator is called
a proper fraction. For any denominator, d, there will be d?1 proper fractions;
for example, with d?=?12:
1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12 .

We shall call a fraction that cannot be cancelled down a resilient fraction.
Furthermore we shall define the resilience of a denominator, R(d), to be the
ratio of its proper fractions that are resilient; for example, R(12) = 4/11.
In fact, d?=?12 is the smallest denominator having a resilience R(d) < 4/10.

Find the smallest denominator d, having a resilience R(d) < 15499/94744."""
from helpers.math_helper import generate_primes, resilience


def solve():
    primes = list(generate_primes(30))

    i = 0
    n = 1
    limit = 15499 / 94744
    while resilience(n * primes[i]) >= limit:
        n *= primes[i]
        i += 1

    for c in (n for n in range(2, primes[i - 1]) if n not in primes):
        if resilience(n * c) < limit:
            return n * c


if __name__ == '__main__':
    print(solve())
