from helpers.math_helper import partitions


def task76():
    return partitions(range(1, 100), 100)


if __name__ == '__main__':
    print(task76())
