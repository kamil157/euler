import unittest

answers_fast = {
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
    12: 76576500,
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
    31: 73682,
    33: 100,
    34: 40730,
    38: 932718654,
    40: 210,
    41: 7652413,
    42: 162,
    45: 1533776805,
    46: 5777,
    49: 296962999629,
    52: 142857,
    53: 4075,
    54: 376,
    55: 249,
    56: 972,
    57: 153,
    79: 73162890,
    97: 8739992577,
    63: 49,
    81: 427337,
    69: 510510,
    71: 428570,
    76: 190569291,
    99: 709,
    243: 892371480,
}

answers_slow = {
    14: 837799,
    23: 4179871,
    24: 2783915460,
    26: 983,
    27: -59231,
    30: 443839,
    32: 45228,
    35: 55,
    36: 872187,
    37: 748317,
    39: 840,
    43: 16695334890,
    44: 5482660,
    47: 134043,
    48: 9110846700,
    50: 997651,
    58: 26241,
    59: 107359,
    92: 8581146,
    206: 1389019170,
}


class TestAnswers(unittest.TestCase):

    def test_answers_fast(self):
        self.run_tests(answers_fast)

    def test_answers_slow(self):
        self.run_tests(answers_slow)

    def run_tests(self, answers):
        for i, answer in answers.items():
            exec("from tasks.task{i} import task{i}".format(i=i))
            self.assertEqual(eval("task" + str(i))(), answer)
