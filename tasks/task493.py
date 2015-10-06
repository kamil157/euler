"""
70 colored balls are placed in an urn, 10 for each of the seven rainbow colors.

What is the expected number of distinct colors in 20 randomly picked balls?

Give your answer with nine digits after the decimal point (a.bcdefghij)."""
from helpers.math_helper import choose


def solve():
    """X = number of colors present
    X = X1 + X2 + ... + X7, where
    Xi = 1 if color i present else 0

    EX = E(X1 + X2 + ... X6)
    EX = EX1 + EX2 + ... + EX6
    EX = 7 * EX1

    EX = 7 * (1 * p(color present))
    EX = 7 * (1 - p(color absent))
    EX = 7 * (1 - #(colors absent) / #(possibilities))
    EX = 7 * (1 - 60 choose 20 / 70 choose 20)
    """
    return round(7 * (1 - choose(60, 20) / choose(70, 20)), 10)


if __name__ == '__main__':
    print(solve())
