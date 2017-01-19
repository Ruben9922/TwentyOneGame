from enum import Enum
from random import randrange
from ruben9922.consoleutilities.inpututilities import input_int


class Suit(Enum):
    Clubs, Diamonds, Hearts, Spades = range(4)

    def __str__(self):
        return self._name_


class Rank(Enum):
    Ace = 1,
    Two = 2,
    Three = 3,
    Four = 4,
    Five = 5,
    Six = 6,
    Seven = 7,
    Eight = 8,
    Nine = 9
    Ten = 10,
    Jack = 11,
    Queen = 12,
    King = 13

    def __str__(self):
        return self._name_


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{} of {}".format(str(self.rank), str(self.suit))


class Deck:
    def __init__(self):
        self.cards = []
        for suit in Suit:
            for rank in Rank:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        cards_temp = []
        for i in range(len(self.cards)):
            card_index = randrange(len(self.cards))
            cards_temp.append(self.cards[card_index])
            self.cards.pop(card_index)
        self.cards = cards_temp

    def __str__(self):
        string_array = []
        prepend_newline = False
        for card in self.cards:
            if prepend_newline:
                string_array.append("\n")
            else:
                prepend_newline = True

            string_array.append(str(card))

        string = "".join(string_array)
        return string


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

# Get player names
player_count = input_int("Number of players: ")
players = []
for i in range(player_count):
    new_player_name = input("Player {} name: ".format(i + 1))
    players.append(Player(new_player_name))
    print("Player \"{}\" created".format(new_player_name))
    print()

# Create deck and shuffle
d = Deck()
d.shuffle()
# print(str(d))
