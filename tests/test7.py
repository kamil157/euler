import unittest

from tasks.task7 import primes


class Test(unittest.TestCase):
    def test_primes(self):
        self.assertEqual(primes(0), [])
        self.assertEqual(primes(1), [])
        self.assertEqual(primes(2), [2])
        self.assertEqual(primes(3), [2, 3])
        self.assertEqual(primes(4), [2, 3])
        self.assertEqual(primes(5), [2, 3, 5])
        self.assertEqual(primes(6), [2, 3, 5])
        self.assertEqual(primes(7), [2, 3, 5, 7])
        self.assertEqual(primes(13), [2, 3, 5, 7, 11, 13])
        self.assertEqual(primes(25), [2, 3, 5, 7, 11, 13, 17, 19, 23])

if __name__ == '__main__':
    unittest.main()