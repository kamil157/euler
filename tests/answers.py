import unittest


answers = {
    1: 233168,
    2: 4613732,
    3: 6857,
    4: 906609,
    5: 232792560,
    6: 25164150,
    7: 104743,
    8: 23514624000,
    9: 31875000,
    10: 142913828922,
    11: 70600674,
    13: 5537376230,
    15: 137846528820,
    16: 1366,
    17: 21124,
    18: 1074,
    19: 171,
    20: 648,
    21: 31626,
    22: 871198282,
    25: 4782,
    28: 669171001,
    29: 9183,
}

answers_slow = {
    12: 76576500,
    14: 837799,
    23: 4179871,
    24: 2783915460,
    26: 983,
    27: -59231,
    30: 443839,
}


class Test(unittest.TestCase):
    def test_answers(self):
        for i, answer in answers.items():
            exec("from tasks.task{i} import task{i}".format(i=i))
            self.assertEqual(eval("task" + str(i))(), answer)

    def test_answers_slow(self):
        for i, answer in answers_slow.items():
            exec("from tasks.task{i} import task{i}".format(i=i))
            self.assertEqual(eval("task" + str(i))(), answer)


if __name__ == '__main__':
    unittest.main()
