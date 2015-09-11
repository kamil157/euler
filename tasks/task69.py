from helpers.math_helper import generate_primes


def task69():
    result = 1
    primes = list(generate_primes(20))

    i = 0
    while result * primes[i] < 1000000:
        result *= primes[i]
        i += 1

    return result


if __name__ == '__main__':
    print(task69())
