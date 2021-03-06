"""Surprisingly there are only three numbers that can be written as the sum
of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits."""


def solve():
    # The maximum value for one digit is 9 ^ 5 = 59049. For 7 digits, the
    # maximum sum would be 7 * 59049 = 413343, which doesn't even come close
    # to 1234567. Therefore the limit is 6 * 9 ^ 5.
    return sum(n for n in range(10, 6 * 9 ** 5)
               if n == sum(int(d) ** 5 for d in str(n)))


if __name__ == '__main__':
    print(solve())
