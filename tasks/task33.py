"""The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which
is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator."""
from fractions import Fraction

from helpers.math_helper import prod


def task33():
    fractions = (Fraction(a, b)
                 for a in range(10, 100)
                 for b in range(a + 1, 100)
                 # non trivial
                 if b % 10 != 0
                 # can be incorrectly simplified
                 if a % 10 == b // 10
                 # incorrectly simplified == correctly simplified
                 if a / b == (a // 10) / (b % 10))
    return prod(fractions).denominator


if __name__ == '__main__':
    print(task33())
