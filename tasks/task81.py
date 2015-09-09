def task81():
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
    print(task81())
