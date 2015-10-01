"""The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit
number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?"""


def solve():
    return len(set(a ** b
                   for a in range(1, 10)
                   for b in range(100)
                   if len(str(a ** b)) == b))


def method_name():
    return


if __name__ == '__main__':
    print(solve())
