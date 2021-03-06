"""Triangle, pentagonal, and hexagonal numbers are generated by the following
formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n?1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n?1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal."""

from helpers.math_helper import pentagonal, hexagonal


def solve():
    # all hexagonal numbers are also triangle
    return next(n for n in set(pentagonal(100000)) & set(hexagonal(100000))
                if n > 40755)


if __name__ == '__main__':
    print(solve())
