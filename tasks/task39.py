"""If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?"""


def triangle_sides():
    for p in range(1, 1000):
        l = []
        for a in range(1, p):
            for b in range(a, p):
                c = p - a - b
                if c > b and a * a + b * b == c * c:
                    l.append((a, b, c))
        yield len(l), p


def task39():
    return max(triangle_sides())[1]


if __name__ == '__main__':
    print(task39())
