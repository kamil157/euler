from tasks.task7 import primes

primes_set = set(primes(100000))


def count_primes(a, b):
    n = 0
    while n * n + a * n + b in primes_set:
        n += 1
    return n


def get_counts():
    for a in range(-999, 1000, 2):
        for b in range(-999, 1000, 2):
            yield count_primes(a, b), a, b

count, a, b = max(get_counts())
print(a * b)