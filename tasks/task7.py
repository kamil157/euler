"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?"""


def primes(limit):
    if limit < 2:
        return []
    a = [True] * (limit + 1)
    a[0] = a[1] = False

    for (i, is_prime) in enumerate(a):
        if is_prime:
            yield i
            for n in range(i * i, limit + 1, i):
                a[n] = False

if __name__ == "__main__":
    print(list(primes(200000))[10000])