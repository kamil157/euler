"""The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t_10. If the word
value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?"""

from helpers.math_helper import word_value


def triangle_numbers(limit):
    return ((x * (x + 1) // 2) for x in range(1, limit))


def solve():
    with open("../res/task42_words.txt") as f:
        words = f.read()[1:-1].split('","')
        triangles = set(triangle_numbers(200))
        return sum(1 for word in words if word_value(word) in triangles)


if __name__ == "__main__":
    print(solve())
