"""An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the
following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000"""
from functools import reduce
from operator import mul


def task40():
    s = ''
    n = 0
    while len(s) <= 1000000:
        s += str(n)
        n += 1
    return reduce(mul, [int(s[10 ** i]) for i in range(7)], 1)


if __name__ == '__main__':
    print(task40())
