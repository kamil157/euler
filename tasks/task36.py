"""The decimal number, 585 = 1001001001(2) (binary), is palindromic in both
bases.

Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)"""


def generate_palindromes():
    for n in range(1000000):
        if str(n) == str(n)[::-1]:
            binary = str(bin(n))[2:]
            if str(binary) == str(binary)[::-1]:
                yield n


print(sum(generate_palindromes()))