"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the
bottom right, by only moving to the right and down, is indicated in bold red
and is equal to 2427.

131 673 234 103  18
201  96 342 965 150
630 803 746 422 111
537 699 497 121 956
805 732 524  37 331

Find the minimal path sum, in matrix.txt (right click and
"Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from
the top left to the bottom right by only moving right and down."""


def solve():
    with open('../res/task81_matrix.txt') as file:
        m = [[int(n) for n in line.split(',')] for line in file]

    for i in range(1, len(m)):
        m[i][0] += m[i - 1][0]
        m[0][i] += m[0][i - 1]

    for i in range(1, len(m)):
        for j in range(1, len(m[0])):
            m[i][j] += min(m[i - 1][j], m[i][j - 1])

    return m[-1][-1]


if __name__ == '__main__':
    print(solve())
