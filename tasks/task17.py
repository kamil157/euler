"""If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance with
British usage."""
from string import ascii_letters

import inflect


def count_letters(n):
    words = inflect.engine().number_to_words(n)
    return sum(1 for c in words if c in ascii_letters)


def task17():
    return sum(count_letters(i) for i in range(1001))


if __name__ == '__main__':
    print(task17())
