"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?"""

# TODO really slow
def primes(n):
    if n < 2:
        return []
    l = set(range(2, n + 1))
    tested = set()

    j = 0
    while j < len(l):
        p = min(l - tested)
        # print(p)
        for i in range(2 * p, n + 1, p):
            if i in l:
                l.remove(i)
        j += 1
        tested.add(p)

    return list(l)

print(primes(110000)[10000])