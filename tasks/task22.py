"""Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?"""


def word_value(word):
    return sum(ord(c) - ord('A') + 1 for c in word)


def task22():
    with open("../res/task22_names.txt") as f:
        s = f.read()
        names = s[1:-1].split('","')
    return sum((i + 1) * word_value(name)
               for i, name in enumerate(sorted(names)))


if __name__ == '__main__':
    print(task22())
