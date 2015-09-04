import unittest

from helpers.math_helper import fib, prime_factors, generate_primes, divisors


class Test(unittest.TestCase):

    def test_fib(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(4), 3)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(20), 6765)
        self.assertEqual(fib(50), 12586269025)
        self.assertEqual(fib(100), 354224848179261915075)

    def test_prime_factors(self):
        self.assertEqual(list(prime_factors(2)), [2])
        self.assertEqual(list(prime_factors(3)), [3])
        self.assertEqual(list(prime_factors(4)), [2, 2])
        self.assertEqual(list(prime_factors(6)), [2, 3])
        self.assertEqual(list(prime_factors(8)), [2, 2, 2])
        self.assertEqual(list(prime_factors(12)), [2, 2, 3])
        self.assertEqual(list(prime_factors(13195)), [5, 7, 13, 29])
        self.assertEqual(list(prime_factors(600851475143)), [71, 839, 1471, 6857])

    def test_primes(self):
        self.assertEqual(list(generate_primes(0)), [])
        self.assertEqual(list(generate_primes(1)), [])
        self.assertEqual(list(generate_primes(2)), [2])
        self.assertEqual(list(generate_primes(3)), [2, 3])
        self.assertEqual(list(generate_primes(4)), [2, 3])
        self.assertEqual(list(generate_primes(5)), [2, 3, 5])
        self.assertEqual(list(generate_primes(6)), [2, 3, 5])
        self.assertEqual(list(generate_primes(7)), [2, 3, 5, 7])
        self.assertEqual(list(generate_primes(13)), [2, 3, 5, 7, 11, 13])
        self.assertEqual(list(generate_primes(25)), [2, 3, 5, 7, 11, 13, 17, 19, 23])

    def test_divisors(self):
        self.assertEqual(divisors(0), set())
        self.assertEqual(divisors(1), {1})
        self.assertEqual(divisors(2), {1, 2})
        self.assertEqual(divisors(4), {1, 2, 4})
        self.assertEqual(divisors(6), {1, 2, 3, 6})
        self.assertEqual(divisors(12), {1, 2, 3, 4, 6, 12})

if __name__ == '__main__':
    unittest.main()
