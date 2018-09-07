import numpy as np

SUITS = {0:'hearts', 1:'diamonds', 2:'clubs', 3:'spades'}
VALUES = {0: '2',
          1: '3', 2: '4', 3: '5', 4: '6',
          5: '7', 6: '8', 7: '9', 8: '10',
          12: 'ace', 9: 'jack', 10: 'queen', 11: 'king'}


class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.get_card_string().split(".")[0];

    def get_card_string(self):
        return VALUES[self.value] + "_of_" + SUITS[self.suit] + ".png"


class Deck:
    def __init__(self):
        self.cards = [None] * 52
        index = 0
        for suit in SUITS:
            for value in VALUES:
                self.cards[index] = Card(value, suit)
                index = index + 1

    def random_sample_cards(self, num_cards):
        return np.random.choice(self.cards, num_cards, replace=False)


class Game:
    def __init__(self, num_players):
        self.num_players = num_players
        self.deck = Deck()
        self.cards = self.deck.random_sample_cards(5+(num_players*2))
        self.flop = self.cards[0:3]
        self.turn = self.cards[3]
        self.river = self.cards[4]
        self.hole_cards = [self.cards[(2*i+5):(2*(i+1)+5)] for i in range(num_players)]

    def get_showdown_cards_of_player(self, player):
        return np.hstack([self.hole_cards[player], self.flop, self.turn, self.river])
