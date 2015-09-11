from helpers.math_helper import generate_primes, resilience


def task243():
    primes = list(generate_primes(30))

    i = 0
    n = 1
    limit = 15499 / 94744
    while resilience(n * primes[i]) >= limit:
        n *= primes[i]
        i += 1

    for c in (n for n in range(2, primes[i - 1]) if n not in primes):
        if resilience(n * c) < limit:
            return n * c


if __name__ == '__main__':
    print(task243())
