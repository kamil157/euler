"""An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the
following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000"""
from helpers.math_helper import prod


def solve():
    concatenated_ints = ''
    n = 0
    while len(concatenated_ints) <= 1000000:
        concatenated_ints += str(n)
        n += 1
    return prod(int(concatenated_ints[10 ** i]) for i in range(7))


if __name__ == '__main__':
    print(solve())
