import unittest

from helpers.math_helper import spiral


class Test(unittest.TestCase):
    def test_sum_diagonals(self):
        self.assertEqual(spiral(1), 1)
        self.assertEqual(spiral(2), 25)
        self.assertEqual(spiral(3), 101)
        self.assertEqual(spiral(4), 261)

if __name__ == '__main__':
    unittest.main()