"""A perfect number is a number for which the sum of its proper divisors
is exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
number.

A number n is called deficient if the sum of its proper divisors is less than
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than
28123 can be written as the sum of two abundant numbers. However, this upper
limit cannot be reduced any further by analysis even though it is known that
the greatest number that cannot be expressed as the sum of two abundant
numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum
of two abundant numbers."""

from tasks.task21 import d as divisor_sum

limit = 28123

abundant_numbers = [i for i in range(2, limit + 1) if divisor_sum(i) > i]


def not_two_abundant(limit):
    numbers = set()
    for i, n in enumerate(abundant_numbers):
        for m in abundant_numbers[i:]:
            k = n + m
            if k <= limit:
                if k not in numbers:
                    numbers.add(k)
            else:
                break
    return numbers


if __name__ == "__main__":
    print(sum((set(range(1, limit)) - not_two_abundant(limit))))
