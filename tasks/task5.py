"""2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?"""


def task5():
    #      9      11   13   16  17   19
    return 2520 * 11 * 13 * 2 * 17 * 19


if __name__ == '__main__':
    print(task5())
