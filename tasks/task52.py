"""It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits."""


def task52():
    n = 1
    while not all(sorted(str(n * i)) == sorted(str(n)) for i in range(2, 7)):
        n += 1
    return n


if __name__ == '__main__':
    print(task52())