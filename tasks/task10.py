from helpers.math_helper import generate_primes


def task10():
    return sum(generate_primes(2000000))


if __name__ == '__main__':
    print(task10())
