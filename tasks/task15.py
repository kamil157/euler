"""Starting in the top left corner of a 2×2 grid, and only being able to move
to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?"""


def task15():
    limit = 20
    m = [[1] * limit for _ in range(limit)]

    for i in range(1, limit):
        for j in range(1, limit):
            m[i][j] = m[i - 1][j] + m[i][j - 1]
    return 2 * sum(m[limit - 1])


if __name__ == '__main__':
    print(task15())
