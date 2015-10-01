"""Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?"""
from helpers.math_helper import word_value


def solve():
    with open("../res/task22_names.txt") as file:
        names = file.read()[1:-1].split('","')
    return sum((i + 1) * word_value(name)
               for i, name in enumerate(sorted(names)))


if __name__ == '__main__':
    print(solve())
