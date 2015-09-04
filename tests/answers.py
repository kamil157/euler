import unittest

from tasks.task1 import task1
from tasks.task2 import task2
from tasks.task3 import task3
from tasks.task4 import task4
from tasks.task5 import task5
from tasks.task6 import task6
from tasks.task7 import task7
from tasks.task8 import task8
from tasks.task9 import task9
from tasks.task10 import task10


class Test(unittest.TestCase):
    def test_answers(self):
        self.assertEqual(task1(), 233168)
        self.assertEqual(task2(), 4613732)
        self.assertEqual(task3(), 6857)
        self.assertEqual(task4(), 906609)
        self.assertEqual(task5(), 232792560)
        self.assertEqual(task6(), 25164150)
        self.assertEqual(task7(), 104743)
        self.assertEqual(task8(), 23514624000)
        self.assertEqual(task9(), 31875000)
        self.assertEqual(task10(), 142913828922)


if __name__ == '__main__':
    unittest.main()
