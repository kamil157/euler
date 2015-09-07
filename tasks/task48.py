"""The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000."""


def task48():
    series_sum = sum([i ** i for i in range(1, 1001)])
    return int(str(series_sum)[-10:])


if __name__ == '__main__':
    print(task48())
