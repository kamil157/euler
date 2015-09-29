"""It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits."""
from itertools import count


def task52():
    return next(n for n in count(1) if contain_same_digits(n))


def contain_same_digits(n):
    return all(sorted(str(n * i)) == sorted(str(n)) for i in range(2, 7))


if __name__ == '__main__':
    print(task52())
