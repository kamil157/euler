import unittest

from tasks.task28 import sum_diagonals


class Test(unittest.TestCase):
    def test_sum_diagonals(self):
        self.assertEqual(sum_diagonals(1), 1)
        self.assertEqual(sum_diagonals(2), 25)
        self.assertEqual(sum_diagonals(3), 101)
        self.assertEqual(sum_diagonals(4), 261)

if __name__ == '__main__':
    unittest.main()