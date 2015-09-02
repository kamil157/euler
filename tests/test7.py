import unittest

from tasks.task7 import generate_primes


class Test(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()