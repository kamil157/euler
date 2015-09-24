"""A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""
from helpers.math_helper import is_palindrome


def task4():
    r = range(100, 1000)
    return max(i * j for i in r for j in r if is_palindrome(i * j))

if __name__ == '__main__':
    print(task4())