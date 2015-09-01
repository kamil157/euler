import unittest

from tasks.task12 import divisors


class Test(unittest.TestCase):
    def test_divisors(self):
        self.assertEqual(divisors(0), set())
        self.assertEqual(divisors(1), {1})
        self.assertEqual(divisors(2), {1, 2})
        self.assertEqual(divisors(4), {1, 2, 4})
        self.assertEqual(divisors(6), {1, 2, 3, 6})
        self.assertEqual(divisors(12), {1, 2, 3, 4, 6, 12})

if __name__ == '__main__':
    unittest.main()