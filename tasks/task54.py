"""In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives
(see example 1 below). But if two ranks tie, for example, both players have
a pair of queens, then highest cards in each hand are compared
(see example 4 below); if the highest cards tie then the next highest cards
are compared, and so on.

Consider the following five hands dealt to two players:
(...)

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space):
the first five are Player 1's cards and the last five are Player 2's cards.
You can assume that all hands are valid (no invalid characters or repeated
cards), each player's hand is in no specific order, and in each hand there
is a clear winner.

How many hands does Player 1 win?"""


def card_value(rank):
    high_cards = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return high_cards[rank] if rank in high_cards else int(rank)


def flush(hand):
    suits = [suit for _, suit in hand]
    return len(set(suits)) == 1


def straight(ranks):
    return card_value(ranks[0]) - card_value(ranks[4]) == 4 \
           and len(set(ranks)) == 5


def kind(hand, n):
    for rank in hand:
        if hand.count(rank) == n:
            return rank
    return False


def two_pairs(ranks):
    high_pair = kind(ranks, 2)
    low_pair = kind(list(reversed(ranks)), 2)
    if high_pair and low_pair != high_pair:
        return high_pair, low_pair
    else:
        return False


def rate_hand(hand):
    ranks = sorted((card_value(rank) for rank, _ in hand), reverse=True)
    if flush(hand) and straight(ranks):
        return 8, ranks
    elif kind(ranks, 4):
        return 7, kind(ranks, 4), ranks
    elif kind(ranks, 3) and kind(ranks, 2):
        return 6, kind(ranks, 3), kind(ranks, 2)
    elif flush(hand):
        return 5, ranks
    elif straight(ranks):
        return 4, ranks
    elif kind(ranks, 3):
        return 3, kind(ranks, 3), ranks
    elif two_pairs(ranks):
        return 2, two_pairs(ranks), ranks
    elif kind(ranks, 2):
        return 1, kind(ranks, 2), ranks
    else:
        return 0, ranks


def solve():
    with open("../res/task54_poker.txt") as file:
        lines = [line.split() for line in file.readlines()]
    return sum(rate_hand(line[:5]) > rate_hand(line[5:]) for line in lines)


if __name__ == '__main__':
    print(solve())
