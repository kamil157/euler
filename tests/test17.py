import unittest

from tasks.task17 import letters


class Test17(unittest.TestCase):
    def test_letters(self):
        self.assertEqual(letters(0), len(""))
        self.assertEqual(letters(1), len("one"))
        self.assertEqual(letters(2), len("two"))
        self.assertEqual(letters(3), len("three"))
        self.assertEqual(letters(10), len("ten"))
        self.assertEqual(letters(11), len("eleven"))
        self.assertEqual(letters(12), len("twelve"))
        self.assertEqual(letters(19), len("nineteen"))
        self.assertEqual(letters(20), len("twenty"))
        self.assertEqual(letters(21), len("twentyone"))
        self.assertEqual(letters(22), len("twentytwo"))
        self.assertEqual(letters(23), len("twentythree"))
        self.assertEqual(letters(33), len("thirtythree"))
        self.assertEqual(letters(99), len("ninetynine"))
        self.assertEqual(letters(100), len("onehundred"))
        self.assertEqual(letters(101), len("onehundredandone"))
        self.assertEqual(letters(102), len("onehundredandtwo"))
        self.assertEqual(letters(122), len("onehundredandtwentytwo"))
        self.assertEqual(letters(199), len("onehundredandninetynine"))
        self.assertEqual(letters(200), len("twohundred"))
        self.assertEqual(letters(201), len("twohundredandone"))
        self.assertEqual(letters(999), len("ninehundredandninetynine"))
        self.assertEqual(letters(1000), len("onethousand"))

