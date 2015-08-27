import unittest

from tasks.task4 import is_palindrome


class Test(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(0))
        self.assertTrue(is_palindrome(11))
        self.assertTrue(is_palindrome(101))
        self.assertTrue(is_palindrome(111))
        self.assertTrue(is_palindrome(1001))
        self.assertTrue(is_palindrome(10101))

        self.assertFalse(is_palindrome(10))
        self.assertFalse(is_palindrome(102))
        self.assertFalse(is_palindrome(1011))
        self.assertFalse(is_palindrome(12131))

if __name__ == '__main__':
    unittest.main()