import unittest
from task2 import fib


class Test1(unittest.TestCase):

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

if __name__ == '__main__':
    unittest.main()