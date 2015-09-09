def sum_square_digits(n):
    s = 0
    while n:
        n, remainder = divmod(n, 10)
        s += remainder * remainder
    return s


def task92():
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
    print(task92())
