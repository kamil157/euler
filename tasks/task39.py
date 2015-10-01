"""If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?"""


def number_of_pythagorean_triples():
    """Based on the relation a^2 + b^2 = c^2.
    If both a and b are even, c will also be even and p will be even.
    If both a and b are odd, c will be even and p will be even.
    If one is even and the other is odd, c will be odd and p will be even.
    Therefore, only even values of p need to be checked."""
    for p in range(2, 1000, 2):
        count = 0
        a = 1
        b = calculate_b(a, p)
        while a < b:
            b = calculate_b(a, p)
            if int(b) == b:
                count += 1
            a += 1
        yield count, p


def calculate_b(a, p):
    """Based on substituting c = p-a-b in equation a^2 + b^2 = c^2
    and transforming it to b = ..."""
    return p * (p - 2 * a) / (2 * (p - a))


def solve():
    return max(number_of_pythagorean_triples())[1]


if __name__ == '__main__':
    print(solve())
