"""The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which
is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator."""

# l = []
# delta = 0.00001
# for a in range(10, 100):
# for b in range(a + 1, 100):
#         if int(str(b)[1]) != 0:
#             for i in range(2):
#                 for j in range(2):
#                     y = int(str(a)[i]) / int(str(b)[j])
#                     if int(str(a)[i-1]) == int(str(b)[j-1]):
#                         if abs(y - a / b) < delta:
#                             l.append((a, b))
#
# print(l)
from functools import reduce
import operator

l = [a / b for a in range(10, 100) for b in range(a + 1, 100) if
     b % 10 != 0 and a % 10 == b // 10 and (a // 10) / (b % 10) == a / b]

print(round(1 / reduce(operator.mul, l, 1)))