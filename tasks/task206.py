"""Find the unique positive integer whose square has the form
1_2_3_4_5_6_7_8_9_0, where each "_" is a single digit."""


def solve():
    s = '1_2_3_4_5_6_7_8_9_0'
    low = int(int(s.replace('_', '0')) ** 0.5)
    high = int(int(s.replace('_', '9')) ** 0.5)
    for n in range(low, high + 1, 10):
        if str(n * n)[::2] == '1234567890':
            return n


if __name__ == '__main__':
    print(solve())
