import unittest

from helpers.math_helper import *


class TestMathHelper(unittest.TestCase):
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
        self.assertEqual(list(prime_factors(600851475143)),
                         [71, 839, 1471, 6857])

    def test_generate_primes(self):
        self.assertEqual(list(generate_primes(0)), [])
        self.assertEqual(list(generate_primes(1)), [])
        self.assertEqual(list(generate_primes(2)), [2])
        self.assertEqual(list(generate_primes(3)), [2, 3])
        self.assertEqual(list(generate_primes(4)), [2, 3])
        self.assertEqual(list(generate_primes(5)), [2, 3, 5])
        self.assertEqual(list(generate_primes(6)), [2, 3, 5])
        self.assertEqual(list(generate_primes(7)), [2, 3, 5, 7])
        self.assertEqual(list(generate_primes(13)), [2, 3, 5, 7, 11, 13])
        self.assertEqual(list(generate_primes(25)),
                         [2, 3, 5, 7, 11, 13, 17, 19, 23])

    def test_divisors(self):
        self.assertEqual(divisors(0), set())
        self.assertEqual(divisors(1), {1})
        self.assertEqual(divisors(2), {1, 2})
        self.assertEqual(divisors(4), {1, 2, 4})
        self.assertEqual(divisors(6), {1, 2, 3, 6})
        self.assertEqual(divisors(12), {1, 2, 3, 4, 6, 12})

    def test_spiral(self):
        self.assertEqual(list(spiral(0)), [1])
        self.assertEqual(list(spiral(1)), [1, 3, 5, 7, 9])
        self.assertEqual(list(spiral(2)), [1, 3, 5, 7, 9, 13, 17, 21, 25])
        self.assertEqual(list(spiral(3))[12], 49)
        self.assertEqual(list(spiral(4))[16], 81)

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(7919))

        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(7907 * 7919))

    def test_partitions(self):
        self.assertEqual(partitions([1], 0), 1)
        self.assertEqual(partitions([1], 1), 1)
        self.assertEqual(partitions([1], 2), 1)
        self.assertEqual(partitions([2], 1), 0)
        self.assertEqual(partitions([2], 2), 1)
        self.assertEqual(partitions([1, 2], 2), 2)
        self.assertEqual(partitions([1, 2], 3), 2)
        self.assertEqual(partitions([1, 2, 3], 3), 3)

    def test_prod(self):
        self.assertEqual(prod([0]), 0)
        self.assertEqual(prod([0, 1]), 0)
        self.assertEqual(prod([1, 2]), 2)
        self.assertEqual(prod(range(1, 5)), 24)
        self.assertEqual(prod([2] * 5), 32)

    def test_resilience(self):
        self.assertEqual(resilience(2), 1)
        self.assertEqual(resilience(3), 1)
        self.assertEqual(resilience(5), 1)
        self.assertEqual(resilience(7), 1)

        self.assertEqual(resilience(4), 2 / 3)
        self.assertEqual(resilience(6), 2 / 5)
        self.assertEqual(resilience(8), 4 / 7)
        self.assertEqual(resilience(12), 4 / 11)

    def test_phi(self):
        self.assertEqual(phi(2), 1)
        self.assertEqual(phi(3), 2)
        self.assertEqual(phi(5), 4)
        self.assertEqual(phi(7), 6)

        self.assertEqual(phi(4), 2)
        self.assertEqual(phi(6), 2)
        self.assertEqual(phi(8), 4)
        self.assertEqual(phi(12), 4)

    def test_proper_divisor_sum(self):
        self.assertEqual(proper_divisor_sum(1), 0)
        self.assertEqual(proper_divisor_sum(2), 1)
        self.assertEqual(proper_divisor_sum(3), 1)
        self.assertEqual(proper_divisor_sum(5), 1)
        self.assertEqual(proper_divisor_sum(7), 1)

        self.assertEqual(proper_divisor_sum(4), 3)
        self.assertEqual(proper_divisor_sum(6), 6)
        self.assertEqual(proper_divisor_sum(10), 8)
        self.assertEqual(proper_divisor_sum(12), 16)
        self.assertEqual(proper_divisor_sum(24), 36)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(''))
        self.assertTrue(is_palindrome('0'))
        self.assertTrue(is_palindrome('11'))
        self.assertTrue(is_palindrome('121'))
        self.assertTrue(is_palindrome('1331'))
        self.assertTrue(is_palindrome('kayak'))
        self.assertTrue(is_palindrome('tacocat'))
        self.assertTrue(is_palindrome('racecar'))
        self.assertTrue(is_palindrome('wasitacaroracatisaw'))

        self.assertTrue(is_palindrome(0))
        self.assertTrue(is_palindrome(11))
        self.assertTrue(is_palindrome(121))
        self.assertTrue(is_palindrome(1331))

    def test_choose(self):
        self.assertEqual(choose(0, 0), 1)
        self.assertEqual(choose(1, 0), 1)
        self.assertEqual(choose(1, 1), 1)
        self.assertEqual(choose(2, 0), 1)
        self.assertEqual(choose(2, 1), 2)
        self.assertEqual(choose(2, 2), 1)
        self.assertEqual(choose(3, 2), 3)
        self.assertEqual(choose(4, 1), 4)
        self.assertEqual(choose(4, 2), 6)
