"""A number chain is created by continuously adding the square of the digits
in a number to form a new number until it has been seen before.

For example,

44 ? 32 ? 13 ? 10 ? 1 ? 1
85 ? 89 ? 145 ? 42 ? 20 ? 4 ? 16 ? 37 ? 58 ? 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless
loop. What is most amazing is that EVERY starting number will eventually
arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?"""


def sum_square_digits(n):
    s = 0
    while n:
        n, remainder = divmod(n, 10)
        s += remainder * remainder
    return s


def solve():
    at1 = set()
    at89 = set()

    limit = 10000000
    for i in range(1, limit):
        n = i
        while n != 1 and n != 89:
            n = sum_square_digits(n)
            if n in at89:
                n = 89
            elif n in at1:
                n = 1
        if n == 89:
            at89.add(i)
        else:
            at1.add(i)
    return sum(1 for n in at89 if n < limit)


if __name__ == '__main__':
    print(solve())
