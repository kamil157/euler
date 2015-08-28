import unittest

from tasks.task7 import primes


class Test(unittest.TestCase):
    def test_primes(self):
        self.assertEqual(list(primes(0)), [])
        self.assertEqual(list(primes(1)), [])
        self.assertEqual(list(primes(2)), [2])
        self.assertEqual(list(primes(3)), [2, 3])
        self.assertEqual(list(primes(4)), [2, 3])
        self.assertEqual(list(primes(5)), [2, 3, 5])
        self.assertEqual(list(primes(6)), [2, 3, 5])
        self.assertEqual(list(primes(7)), [2, 3, 5, 7])
        self.assertEqual(list(primes(13)), [2, 3, 5, 7, 11, 13])
        self.assertEqual(list(primes(25)), [2, 3, 5, 7, 11, 13, 17, 19, 23])

if __name__ == '__main__':
    unittest.main()