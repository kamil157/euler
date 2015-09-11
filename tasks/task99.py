import math


def task99():
    with open("../res/task99_base_exp.txt") as file:
        numbers = [[int(n) for n in line.split(',')] for line in file]

    result = max((exp * math.log10(base), base, exp) for base, exp in numbers)
    return numbers.index([result[1], result[2]]) + 1


if __name__ == '__main__':
    print(task99())
