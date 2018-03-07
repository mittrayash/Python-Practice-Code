import collections
from random import choice

# Creates classes without functions; but only attributes (like a database)
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(x) for x in range(2, 11)] + list('JQKA')
    suits = 'Hearts Spades Diamonds Clubs'.split()

    def __init__(self):
        self._cards = [Card(rank, suits) for rank in self.ranks for suits in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, pos):
        return self._cards[pos]


fff = FrenchDeck()
print(fff[3])
print(len(fff))
# Generates random output from the collection
print(choice(fff))

# SORTING
suit_vals = dict(Spades=3, Hearts=2, Diamonds=1, Clubs=0)
print(suit_vals)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)

    return rank_value * len(suit_vals) + suit_vals[card.suit]


for card in sorted(fff, key=spades_high):

    print(card)
