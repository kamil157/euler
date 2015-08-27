import unittest

from tasks.task1 import multiples


class Test1(unittest.TestCase):

    def test_multiples(self):
        self.assertEqual(list(multiples(0)), [])
        self.assertEqual(list(multiples(10)), [3, 5, 6, 9])
        self.assertEqual(list(multiples(20)), [3, 5, 6, 9, 10, 12, 15, 18])
        self.assertEqual(sum(multiples(1000)), 233168)

if __name__ == '__main__':
    unittest.main()