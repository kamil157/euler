"""The decimal number, 585 = 1001001001(2) (binary), is palindromic in both
bases.

Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)"""
from helpers.math_helper import is_palindrome


def generate_palindromes():
    return (n for n in range(1000000)
            if is_palindrome(n)
            if is_palindrome(bin(n)[2:]))


def task36():
    return sum(generate_palindromes())


if __name__ == '__main__':
    print(task36())
