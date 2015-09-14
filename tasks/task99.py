"""Comparing two numbers written in index form like 2^11 and 3^7 is not
difficult, as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more
difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file
containing one thousand lines with a base/exponent pair on each line,
determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example
given above."""
import math


def task99():
    with open("../res/task99_base_exp.txt") as file:
        numbers = [[int(n) for n in line.split(',')] for line in file]

    result = max((exp * math.log10(base), base, exp) for base, exp in numbers)
    return numbers.index([result[1], result[2]]) + 1


if __name__ == '__main__':
    print(task99())
