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
from tasks.task7 import generate_primes

limit = 10000
primes = set(generate_primes(limit))
odd_composites = [n for n in range(2, limit) if n not in primes and n % 2 != 0]

print(next(n for n in odd_composites if all(
    n - 2 * i ** 2 not in primes for i in range(1, int(n ** 0.5)))))
