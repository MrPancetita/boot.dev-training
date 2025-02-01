import random

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_value = RANKS.index(rank)
        self.suit_value = SUITS.index(suit)

    def __eq__(self, other):
        if self.rank_value == other.rank_value and self.suit_value == other.suit_value:
            return True
        return False

    def __lt__(self, other):
        if self.rank_value < other.rank_value:
            return True
        elif self.rank_value == other.rank_value:
            if self.suit_value < other.suit_value:
                return True
        return False

    def __gt__(self, other):
        if self.rank_value > other.rank_value:
            return True
        elif self.rank_value == other.rank_value:
            if self.suit_value > other.suit_value:
                return True
        return False

    # don't touch below this line

    def __str__(self):
        return f"{self.rank} of {self.suit}"
