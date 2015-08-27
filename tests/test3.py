import unittest

from tasks.task3 import prime_factors


class Test(unittest.TestCase):

    def test_prime_factors(self):
        self.assertEqual(prime_factors(2), [2])
        self.assertEqual(prime_factors(3), [3])
        self.assertEqual(prime_factors(4), [2, 2])
        self.assertEqual(prime_factors(6), [2, 3])
        self.assertEqual(prime_factors(8), [2, 2, 2])
        self.assertEqual(prime_factors(12), [2, 2, 3])
        self.assertEqual(prime_factors(13195), [5, 7, 13, 29])
        self.assertEqual(prime_factors(600851475143), [71, 839, 1471, 6857])

if __name__ == '__main__':
    unittest.main()