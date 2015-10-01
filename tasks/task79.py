"""
A common security method used for online banking is to ask the user for three
random characters from a passcode. For example, if the passcode was 531278,
they may ask for the 2nd, 3rd, and 5th characters; the expected reply would
be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse
the file so as to determine the shortest possible secret passcode of unknown
length."""


def solve():
    with open("../res/task79_keylog.txt") as file:
        keys = [line for line in file.read().split()]

    guess = 73162890
    for key in keys:
        pos = [str(guess).find(c) for c in key]
        if pos != sorted(pos):
            print(key, "fail")
            return

    return guess


if __name__ == '__main__':
    print(solve())
