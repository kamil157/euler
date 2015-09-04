from helpers.math_helper import generate_primes


def count_primes(a, b, primes):
    n = 0
    while n * n + a * n + b in primes:
        n += 1
    return n


def get_counts():
    primes = set(generate_primes(100000))
    for a in range(-999, 1000, 2):
        for b in range(-999, 1000, 2):
            yield count_primes(a, b, primes), a, b


def task27():
    count, a, b = max(get_counts())
    return a * b


if __name__ == '__main__':
    print(task27())
