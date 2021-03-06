import unittest
import numpy as np
from pokerlib.Evalutaor import evaluate_cards
from pokerlib.DecisionMaker import decide_on_victory
from pokerlib.domain import Card

# SUITS = {0:'hearts', 1:'diamonds', 2:'clubs', 3:'spades'}
# VALUES = {0: '2',
#           1: '3', 2: '4', 3: '5', 4: '6',
#           5: '7', 6: '8', 7: '9', 8: '10',
#           12: 'ace', 9: 'jack', 10: 'queen', 11: 'king'}
# ROYAL_FLUSH = 9
# STRAIGHT_FLUSH = 8
# FOUR_OF_A_KIND = 7
# FULL_HOUSE = 6
# FLUSH = 5
# STRAIGHT = 4
# THREE_OF_A_KIND = 3
# TWO_PAIR = 2
# PAIR = 1
# HIGH_CARD = 0
class TestBorderConditions(unittest.TestCase):

    def testIndexErrorStraightFlush(self):
        cards = [[Card(0, 3), Card(1, 2), Card(2, 2), Card(3, 2), Card(4, 2), Card(6, 0), Card(6, 2)],
                 [Card(1, 2), Card(2, 2), Card(3, 2), Card(4, 2), Card(5, 1), Card(6, 2), Card(8, 3)],
                 [Card(1, 2), Card(2, 2), Card(3, 2), Card(4, 2), Card(5, 2), Card(6, 2), Card(12, 0)],
                 [Card(0, 0), Card(1, 2), Card(2, 2), Card(3, 2), Card(4, 2), Card(6, 2), Card(7, 2)],
                 [Card(1, 3), Card(1, 2), Card(2, 2), Card(3, 2), Card(4, 2), Card(6, 2), Card(7, 1)],
                 [Card(1, 2), Card(2, 2), Card(3, 2), Card(4, 2), Card(6, 2), Card(7, 3), Card(10, 1)],
                 [Card(1, 2), Card(2, 1), Card(2, 2), Card(3, 2), Card(4, 2), Card(6, 2), Card(9, 1)],
                 [Card(1, 2), Card(2, 2), Card(3, 2), Card(4, 2), Card(6, 2), Card(11, 0), Card(12, 2)],
                 [Card(0, 2), Card(1, 2), Card(2, 2), Card(3, 2), Card(4, 2), Card(6, 2), Card(10, 0)]]
        cards_eval = [evaluate_cards(card) for card in cards]
        self.assertEqual(cards_eval[0][0], 5, cards_eval[0])
        self.assertEqual(cards_eval[1][0], 5, cards_eval[1])
        self.assertEqual(cards_eval[2][0], 8, cards_eval[2])
        self.assertEqual(cards_eval[3][0], 5, cards_eval[3])
        self.assertEqual(cards_eval[4][0], 5, cards_eval[4])
        self.assertEqual(cards_eval[5][0], 5, cards_eval[5])
        self.assertEqual(cards_eval[6][0], 5, cards_eval[6])
        self.assertEqual(cards_eval[7][0], 5, cards_eval[7])
        self.assertEqual(cards_eval[8][0], 8, cards_eval[8])
        winning_indexes = decide_on_victory(cards_eval)
        assert (winning_indexes[0] == 2)
        assert (len(winning_indexes) == 1)


    def testNoWinnerWithQuads(self):
        cards = [[Card(4, 0), Card(5, 2), Card(5, 0), Card(5, 3), Card(5, 1), Card(6, 0), Card(9, 3)],
                 [Card(0, 2), Card(4, 1), Card(5, 2), Card(5, 0), Card(5, 3), Card(5, 1), Card(9, 3)],
                 [Card(1, 1), Card(2, 3), Card(5, 2), Card(5, 0), Card(5, 3), Card(5, 1), Card(9, 3)],
                 [Card(5, 2), Card(5, 0), Card(5, 3), Card(5, 1), Card(9, 2), Card(9, 0), Card(9, 3)],
                 [Card(0, 1), Card(5, 2), Card(5, 0), Card(5, 3), Card(5, 1), Card(9, 3), Card(11, 0)],
                 [Card(1, 2), Card(5, 2), Card(5, 0), Card(5, 3), Card(5, 1), Card(6, 2), Card(9, 3)],
                 [Card(5, 2), Card(5, 0), Card(5, 3), Card(5, 1), Card(6, 3), Card(9, 3), Card(12, 0)],
                 [Card(0, 0), Card(4, 2), Card(5, 2), Card(5, 0), Card(5, 3),  Card(5, 1), Card(9, 3)],
                 [Card(5, 2), Card(5, 0), Card(5, 3), Card(5, 1), Card(6, 1), Card(9, 1), Card(9, 3)]]
        cards_eval = [evaluate_cards(card) for card in cards]
        self.assertEqual(cards_eval[0][0], 7, cards_eval[0])
        self.assertEqual(cards_eval[1][0], 7, cards_eval[1])
        self.assertEqual(cards_eval[2][0], 7, cards_eval[2])
        self.assertEqual(cards_eval[3][0], 7, cards_eval[3])
        self.assertEqual(cards_eval[4][0], 7, cards_eval[4])
        self.assertEqual(cards_eval[5][0], 7, cards_eval[5])
        self.assertEqual(cards_eval[6][0], 7, cards_eval[6])
        self.assertEqual(cards_eval[7][0], 7, cards_eval[7])
        self.assertEqual(cards_eval[8][0], 7, cards_eval[8])
        winning_indexes = decide_on_victory(cards_eval)
        assert (winning_indexes[0] == 6)
        assert (len(winning_indexes) == 1)

    def testNoWinnerBecauseOfPairKickerBug(self):
        cards = [[Card(0, 0), Card(2, 2), Card(3, 3), Card(8, 1), Card(9, 2), Card(9, 0), Card(11, 2)],
                 [Card(0, 0), Card(1, 0), Card(3, 3), Card(4, 1), Card(9, 2), Card(9, 0), Card(11, 2)],
                 [Card(0, 0), Card(3, 3), Card(5, 1), Card(9, 2), Card(9, 0), Card(11, 2), Card(12, 0)],
                 [Card(0, 0), Card(1, 1), Card(3, 3), Card(9, 2), Card(9, 0), Card(11, 2), Card(12, 2)],
                 [Card(0, 0), Card(3, 3), Card(6, 2), Card(9, 2), Card(9, 0), Card(10, 2), Card(11, 2)],
                 [Card(0, 0), Card(3, 3), Card(4, 2), Card(7, 3), Card(9, 2), Card(9, 0), Card(11, 2)],
                 [Card(0, 0), Card(3, 3), Card(6, 3), Card(8, 0), Card(9, 2), Card(9, 0), Card(11, 2)],
                 [Card(0, 0), Card(3, 3), Card(5, 2), Card(7, 0), Card(9, 2), Card(9, 0), Card(11, 2)],
                 [Card(0, 0), Card(3, 3), Card(5, 3), Card(9, 2), Card(9, 0), Card(11, 2), Card(12, 1)]]
        cards_eval = [evaluate_cards(card) for card in cards]
        self.assertEqual(cards_eval[0][0], 1, cards_eval[0])
        self.assertEqual(cards_eval[1][0], 1, cards_eval[1])
        self.assertEqual(cards_eval[2][0], 1, cards_eval[2])
        self.assertEqual(cards_eval[3][0], 1, cards_eval[3])
        self.assertEqual(cards_eval[4][0], 1, cards_eval[4])
        self.assertEqual(cards_eval[5][0], 1, cards_eval[5])
        self.assertEqual(cards_eval[6][0], 1, cards_eval[6])
        self.assertEqual(cards_eval[7][0], 1, cards_eval[7])
        self.assertEqual(cards_eval[8][0], 1, cards_eval[8])
        winning_indexes = decide_on_victory(cards_eval)
        assert (winning_indexes[0] == 2)
        assert (winning_indexes[1] == 8)
        assert (len(winning_indexes) == 2)

    def testNoWinnerBecauseOfKickerSelectionBug(self):
        cards = [[Card(0, 3), Card(1, 2), Card(4, 3), Card(5, 0), Card(7, 3), Card(12, 1), Card(12, 0)],
                 [Card(0, 3), Card(1, 1), Card(4, 3), Card(7, 3), Card(9, 1), Card(12, 1), Card(12, 0)],
                 [Card(0, 3), Card(3, 2), Card(4, 3), Card(7, 3), Card(8, 1), Card(12, 1), Card(12, 0)],
                 [Card(0, 3), Card(4, 3), Card(6, 3), Card(7, 3), Card(8, 2), Card(12, 1), Card(12, 0)],
                 [Card(0, 3), Card(4, 3), Card(7, 3), Card(8, 3), Card(10, 1), Card(12, 1), Card(12, 0)],
                 [Card(0, 3), Card(4, 3), Card(5, 2), Card(7, 3), Card(10, 3), Card(12, 1), Card(12, 0)],
                 [Card(0, 3), Card(2, 2), Card(4, 3), Card(7, 3), Card(11, 1), Card(12, 1), Card(12, 0)],
                 [Card(0, 3), Card(4, 3), Card(7, 3), Card(8, 0), Card(9, 2), Card(12, 1), Card(12, 0)],
                 [Card(0, 3), Card(3, 1), Card(4, 3), Card(7, 3), Card(11, 2), Card(12, 1), Card(12, 0)]]
        cards_eval = [evaluate_cards(card) for card in cards]
        self.assertEqual(cards_eval[0][0], 1, cards_eval[0])
        self.assertEqual(cards_eval[1][0], 1, cards_eval[1])
        self.assertEqual(cards_eval[2][0], 1, cards_eval[2])
        self.assertEqual(cards_eval[3][0], 1, cards_eval[3])
        self.assertEqual(cards_eval[4][0], 1, cards_eval[4])
        self.assertEqual(cards_eval[5][0], 1, cards_eval[5])
        self.assertEqual(cards_eval[6][0], 1, cards_eval[6])
        self.assertEqual(cards_eval[7][0], 1, cards_eval[7])
        self.assertEqual(cards_eval[8][0], 1, cards_eval[8])
        winning_indexes = decide_on_victory(cards_eval)
        assert (winning_indexes[0] == 6)
        assert (winning_indexes[1] == 8)
        assert (len(winning_indexes) == 2)

    def testIndexOutOfBoundsDueToIncorrectKickerHandling(self):
        cards = [[Card(0, 2), Card(1, 1), Card(6, 2), Card(7, 0), Card(9, 1), Card(12, 1), Card(12, 3)],
                 [Card(0, 2), Card(1, 1), Card(2, 0), Card(7, 0), Card(9, 1), Card(11, 0), Card(12, 3)],
                 [Card(0, 2), Card(1, 1), Card(7, 0), Card(9, 1), Card(10, 1), Card(12, 0), Card(12, 3)],
                 [Card(0, 2), Card(1, 1), Card(2, 2), Card(4, 2), Card(7, 0), Card(9, 1), Card(12, 3)],
                 [Card(0, 2), Card(1, 1), Card(4, 3), Card(7, 0), Card(8, 1), Card(9, 1), Card(12, 3)],
                 [Card(0, 3), Card(0, 2), Card(1, 1), Card(7, 0), Card(8, 2), Card(9, 1), Card(12, 3)],
                 [Card(0, 2), Card(1, 1), Card(7, 0), Card(9, 1), Card(10, 2), Card(12, 2), Card(12, 3)],
                 [Card(0, 2), Card(1, 1), Card(2, 1), Card(6, 1), Card(7, 0), Card(9, 1), Card(12, 3)],
                 [Card(0, 2), Card(1, 1), Card(5, 2), Card(7, 0), Card(9, 0), Card(9, 1), Card(12, 3)]]
        cards_eval = [evaluate_cards(card) for card in cards]
        self.assertEqual(cards_eval[0][0], 1, cards_eval[0])
        self.assertEqual(cards_eval[1][0], 0, cards_eval[1])
        self.assertEqual(cards_eval[2][0], 1, cards_eval[2])
        self.assertEqual(cards_eval[3][0], 0, cards_eval[3])
        self.assertEqual(cards_eval[4][0], 0, cards_eval[4])
        self.assertEqual(cards_eval[5][0], 1, cards_eval[5])
        self.assertEqual(cards_eval[6][0], 1, cards_eval[6])
        self.assertEqual(cards_eval[7][0], 0, cards_eval[7])
        self.assertEqual(cards_eval[8][0], 1, cards_eval[8])
        winning_indexes = decide_on_victory(cards_eval)
        assert (winning_indexes[0] == 2)
        assert (winning_indexes[1] == 6)
        assert (len(winning_indexes) == 2)

    def testNoWinnerWithTwoPairs(self):
        cards = [[Card(0, 3), Card(1, 1), Card(4, 0), Card(4, 2), Card(7, 1), Card(12, 1), Card(12, 3)],
                 [Card(1, 3), Card(1, 1), Card(4, 0), Card(4, 2), Card(7, 2), Card(7, 1), Card(12, 3)],
                 [Card(1, 1), Card(4, 0), Card(4, 2), Card(5, 0), Card(7, 1), Card(8, 3), Card(12, 3)],
                 [Card(1, 1), Card(2, 2), Card(4, 0), Card(4, 2), Card(7, 1), Card(9, 1), Card(12, 3)],
                 [Card(1, 1), Card(4, 0), Card(4, 2), Card(7, 1), Card(11, 2), Card(12, 0), Card(12, 3)],
                 [Card(1, 1), Card(4, 0), Card(4, 2), Card(6, 3), Card(7, 1), Card(9, 0), Card(12, 3)],
                 [Card(1, 1), Card(3, 1), Card(4, 0), Card(4, 2), Card(5, 2), Card(7, 1), Card(12, 3)],
                 [Card(1, 1), Card(4, 0), Card(4, 2), Card(7, 0), Card(7, 1), Card(8, 2), Card(12, 3)],
                 [Card(0, 1), Card(1, 1), Card(3, 2), Card(4, 0), Card(4, 2), Card(7, 1), Card(12, 3)]]
        cards_eval = [evaluate_cards(card) for card in cards]
        self.assertEqual(cards_eval[0][0], 2, cards_eval[0])
        self.assertEqual(cards_eval[1][0], 2, cards_eval[1])
        self.assertEqual(cards_eval[2][0], 1, cards_eval[2])
        self.assertEqual(cards_eval[3][0], 1, cards_eval[3])
        self.assertEqual(cards_eval[4][0], 2, cards_eval[4])
        self.assertEqual(cards_eval[5][0], 1, cards_eval[5])
        self.assertEqual(cards_eval[6][0], 1, cards_eval[6])
        self.assertEqual(cards_eval[7][0], 2, cards_eval[7])
        self.assertEqual(cards_eval[8][0], 1, cards_eval[8])
        winning_indexes = decide_on_victory(cards_eval)
        assert (winning_indexes[0] == 4)
        assert (len(winning_indexes) == 1)

    def testIndexErrorThreeOfAKind(self):
        cards = [[Card(1, 0), Card(4, 3), Card(5, 2), Card(5, 1), Card(5, 0), Card(6, 0), Card(10, 1)],
                 [Card(3, 2), Card(5, 2), Card(5, 1), Card(5, 0), Card(6, 0), Card(10, 1), Card(12, 0)],
                 [Card(1, 2), Card(5, 2), Card(5, 1), Card(5, 0), Card(6, 0), Card(9, 2), Card(10, 1)],
                 [Card(4, 0), Card(5, 2), Card(5, 1), Card(5, 0), Card(6, 0), Card(9, 3), Card(10, 1)],
                 [Card(5, 2), Card(5, 1), Card(5, 0), Card(6, 0), Card(8, 3), Card(10, 1), Card(12, 3)],
                 [Card(2, 2), Card(5, 2), Card(5, 1), Card(5, 0), Card(6, 0), Card(10, 1), Card(11, 0)],
                 [Card(0, 1), Card(5, 2), Card(5, 1), Card(5, 0), Card(6, 0), Card(10, 1), Card(11, 3)],
                 [Card(2, 3), Card(5, 2), Card(5, 1), Card(5, 0), Card(6, 0), Card(10, 1), Card(11, 1)],
                 [Card(1, 3), Card(2, 0), Card(5, 2), Card(5, 1), Card(5, 0), Card(6, 0), Card(10, 1)]]
        cards_eval = [evaluate_cards(card) for card in cards]
        self.assertEqual(cards_eval[0][0], 3, cards_eval[0])
        self.assertEqual(cards_eval[1][0], 3, cards_eval[1])
        self.assertEqual(cards_eval[2][0], 3, cards_eval[2])
        self.assertEqual(cards_eval[3][0], 3, cards_eval[3])
        self.assertEqual(cards_eval[4][0], 3, cards_eval[4])
        self.assertEqual(cards_eval[5][0], 3, cards_eval[5])
        self.assertEqual(cards_eval[6][0], 3, cards_eval[6])
        self.assertEqual(cards_eval[7][0], 3, cards_eval[7])
        self.assertEqual(cards_eval[8][0], 3, cards_eval[8])
        winning_indexes = decide_on_victory(cards_eval)
        assert (winning_indexes[0] == 1)
        assert (winning_indexes[1] == 4)
        assert (len(winning_indexes) == 2)

    def testNoWinnerSinglePair9Handed(self):
        cards = [[Card(0, 0), Card(5, 0), Card(6, 2), Card(7, 3), Card(9, 2), Card(10, 0), Card(11, 2)],
                 [Card(0, 1), Card(0, 0), Card(3, 0), Card(7, 3), Card(9, 2), Card(10, 0), Card(11, 2)],
                 [Card(0, 0), Card(6, 1), Card(7, 3), Card(9, 2), Card(10, 0), Card(11, 2), Card(12, 1)],
                 [Card(0, 0), Card(2, 2), Card(2, 3), Card(7, 3), Card(9, 2), Card(10, 0), Card(11, 2)],
                 [Card(0, 0), Card(4, 0), Card(4, 2), Card(7, 3), Card(9, 2), Card(10, 0), Card(11, 2)],
                 [Card(0, 0), Card(4, 1), Card(7, 3), Card(9, 1), Card(9, 2), Card(10, 0), Card(11, 2)],
                 [Card(0, 0), Card(5, 1), Card(7, 3), Card(9, 0), Card(9, 2), Card(10, 0), Card(11, 2)],
                 [Card(0, 3), Card(0, 0), Card(6, 3), Card(7, 3), Card(9, 2), Card(10, 0), Card(11, 2)],
                 [Card(0, 0), Card(1, 1), Card(7, 3), Card(9, 2), Card(10, 0), Card(11, 2), Card(12, 2)]]
        cards_eval = [evaluate_cards(card) for card in cards]
        self.assertEqual(cards_eval[0][0], 0, cards_eval[0])
        self.assertEqual(cards_eval[1][0], 1, cards_eval[1])
        self.assertEqual(cards_eval[2][0], 0, cards_eval[2])
        self.assertEqual(cards_eval[3][0], 1, cards_eval[3])
        self.assertEqual(cards_eval[4][0], 1, cards_eval[4])
        self.assertEqual(cards_eval[5][0], 1, cards_eval[5])
        self.assertEqual(cards_eval[6][0], 1, cards_eval[6])
        self.assertEqual(cards_eval[7][0], 1, cards_eval[7])
        self.assertEqual(cards_eval[8][0], 0, cards_eval[8])
        winning_indexes = decide_on_victory(cards_eval)
        assert (winning_indexes[0] == 5)
        assert (winning_indexes[1] == 6)
        assert (len(winning_indexes) == 2)

    def testNoWinnerInTwoPair9Handed(self):
        cards = [[Card(0, 3), Card(4, 2), Card(6, 0), Card(9, 2), Card(9, 3), Card(10, 1), Card(10, 0)],
                 [Card(0, 3), Card(4, 2), Card(7, 0), Card(8, 3), Card(9, 2), Card(9, 3), Card(10, 0)],
                 [Card(0, 3), Card(4, 2), Card(7, 3), Card(9, 2), Card(9, 3), Card(10, 0), Card(12, 2)],
                 [Card(0, 3), Card(4, 2), Card(8, 1), Card(9, 2), Card(9, 3), Card(10, 0), Card(11, 2)],
                 [Card(0, 3), Card(4, 2), Card(8, 2), Card(9, 2), Card(9, 3), Card(10, 0), Card(12, 1)],
                 [Card(0, 3), Card(3, 3), Card(4, 2), Card(9, 2), Card(9, 3), Card(10, 3), Card(10, 0)],
                 [Card(0, 3), Card(1, 0), Card(4, 2), Card(9, 2), Card(9, 3), Card(10, 0), Card(12, 0)],
                 [Card(0, 3), Card(4, 2), Card(8, 0), Card(9, 2), Card(9, 3), Card(10, 2), Card(10, 0)],
                 [Card(0, 3), Card(3, 1), Card(3, 0), Card(4, 2), Card(9, 2), Card(9, 3), Card(10, 0)]]
        cards_eval = [evaluate_cards(card) for card in cards]
        self.assertEqual(cards_eval[0][0], 2, cards_eval[0])
        self.assertEqual(cards_eval[1][0], 1, cards_eval[1])
        self.assertEqual(cards_eval[2][0], 1, cards_eval[2])
        self.assertEqual(cards_eval[3][0], 1, cards_eval[3])
        self.assertEqual(cards_eval[4][0], 1, cards_eval[4])
        self.assertEqual(cards_eval[5][0], 2, cards_eval[5])
        self.assertEqual(cards_eval[6][0], 1, cards_eval[6])
        self.assertEqual(cards_eval[7][0], 2, cards_eval[7])
        self.assertEqual(cards_eval[8][0], 2, cards_eval[8])
        winning_indexes = decide_on_victory(cards_eval)
        assert (winning_indexes[0] == 7)
        assert (len(winning_indexes) == 1)

    def testManyPairsException(self):
        cards = [[Card(5, 3), Card(5, 0), Card(8, 2), Card(8, 1), Card(9, 1), Card(10, 3), Card(10, 1)],
                 [Card(3, 0), Card(5, 1), Card(5, 0), Card(8, 2), Card(8, 1), Card(9, 1), Card(10, 1)],
                 [Card(5, 0), Card(8, 2), Card(8, 1), Card(9, 1), Card(10, 1), Card(11, 1), Card(12, 1)],
                 [Card(0, 2), Card(4, 1), Card(5, 0), Card(8, 2), Card(8, 1), Card(9, 1), Card(10, 1)],
                 [Card(1, 0), Card(5, 0), Card(8, 2), Card(8, 1), Card(9, 2), Card(9, 1), Card(10, 1)],
                 [Card(3, 1), Card(5, 0), Card(8, 2), Card(8, 1), Card(9, 1), Card(10, 0), Card(10, 1)]]
        cards_eval = [evaluate_cards(card) for card in cards]
        self.assertEqual(cards_eval[0][0], 2, cards_eval[0])
        self.assertEqual(cards_eval[1][0], 2, cards_eval[1])
        self.assertEqual(cards_eval[2][0], 9, cards_eval[2])
        self.assertEqual(cards_eval[3][0], 1, cards_eval[3])
        self.assertEqual(cards_eval[4][0], 2, cards_eval[4])
        self.assertEqual(cards_eval[5][0], 2, cards_eval[5])
        winning_indexes = decide_on_victory(cards_eval)
        assert (winning_indexes[0] == 2)
        assert (len(winning_indexes) == 1)

    def testNoFinalFlushStateException(self):
        cards = [[Card(0, 2), Card(4, 3), Card(9, 1), Card(10, 2), Card(11, 2), Card(12, 1), Card(12, 2)],
                 [Card(0, 0), Card(0, 2), Card(3, 1), Card(4, 3), Card(10, 2), Card(11, 2), Card(12, 2)],
                 [Card(0, 2), Card(1, 0), Card(4, 3), Card(6, 3), Card(10, 2), Card(11, 2), Card(12, 2)],
                 [Card(0, 2), Card(3, 3), Card(4, 3), Card(5, 3), Card(10, 2), Card(11, 2), Card(12, 2)],
                 [Card(0, 2), Card(4, 3), Card(8, 3), Card(9, 2), Card(10, 2), Card(11, 2), Card(12, 2)],
                 [Card(0, 2), Card(3, 0), Card(4, 3), Card(10, 2), Card(11, 2), Card(12, 0), Card(12, 2)]]
        cards_eval = [evaluate_cards(card) for card in cards]
        self.assertEqual(cards_eval[0][0], 1, cards_eval[0])
        self.assertEqual(cards_eval[1][0], 1, cards_eval[1])
        self.assertEqual(cards_eval[2][0], 0, cards_eval[2])
        self.assertEqual(cards_eval[3][0], 0, cards_eval[3])
        self.assertEqual(cards_eval[4][0], 5, cards_eval[4])
        self.assertEqual(cards_eval[5][0], 1, cards_eval[5])
        winning_indexes = decide_on_victory(cards_eval)
        assert (winning_indexes[0] == 4)
        assert (len(winning_indexes) == 1)

    def testStraightIndexes(self):
        cards = [[Card(2, 2), Card(6, 2), Card(7, 1), Card(8, 3), Card(9, 1), Card(10, 1), Card(12, 1)],
                 [Card(1, 1), Card(2, 3), Card(7, 1), Card(8, 3), Card(9, 1), Card(10, 1), Card(12, 1)],
                 [Card(0, 0), Card(6, 1), Card(7, 1), Card(8, 3), Card(9, 1), Card(10, 1), Card(12, 1)],
                 [Card(0, 2), Card(7, 1), Card(8, 3), Card(9, 1), Card(10, 1), Card(11, 1), Card(12, 1)],
                 [Card(2, 0), Card(7, 1), Card(8, 3), Card(9, 1), Card(10, 1), Card(11, 2), Card(12, 1)],
                 [Card(1, 3), Card(4, 3), Card(7, 1), Card(8, 3), Card(9, 1),  Card(10, 1), Card(12, 1)]]
        cards_eval = [evaluate_cards(card) for card in cards]
        self.assertEqual(cards_eval[0][0], 4, cards_eval[0])
        self.assertEqual(cards_eval[1][0], 5, cards_eval[1])
        self.assertEqual(cards_eval[2][0], 5, cards_eval[2])
        self.assertEqual(cards_eval[3][0], 5, cards_eval[3])
        self.assertEqual(cards_eval[4][0], 4, cards_eval[4])
        self.assertEqual(cards_eval[5][0], 0, cards_eval[5])
        winning_indexes = decide_on_victory(cards_eval)
        assert (winning_indexes[0] == 3)
        assert (len(winning_indexes) == 1)

    def testFlushEvaluation(self):
        cards = [
            [Card(1, 2), Card(3, 0), Card(7, 2), Card(8, 2), Card(9, 3), Card(10, 1), Card(11, 2)],
            [Card(1, 2), Card(4, 1), Card(6, 1), Card(8, 2), Card(9, 3), Card(10, 1), Card(11, 2)],
            [Card(1, 2), Card(6, 3), Card(8, 1), Card(8, 2), Card(9, 3), Card(10, 1), Card(11, 2)],
            [Card(0, 0), Card(1, 2), Card(8, 2), Card(9, 3), Card(10, 1), Card(11, 2), Card(12, 0)],
            [Card(0, 2), Card(1, 2), Card(8, 2), Card(9, 3), Card(10, 1), Card(11, 2), Card(12, 2)],
            [Card(1, 2), Card(2, 3), Card(5, 0), Card(8, 2), Card(9, 3), Card(10, 1), Card(11, 2)]]
        cards_eval = [evaluate_cards(card) for card in cards]
        assert (cards_eval[0][0] == 4)
        assert (cards_eval[1][0] == 0)
        assert (cards_eval[2][0] == 1)
        assert (cards_eval[3][0] == 4)
        assert (cards_eval[4][0] == 5)
        assert (cards_eval[5][0] == 0)
        winning_indexes = decide_on_victory(cards_eval)
        assert (winning_indexes[0] == 4)
        assert (len(winning_indexes) == 1)

    def testFullHouseSetsIndexError(self):
        cards = [[Card(2, 2), Card(2, 3), Card(3, 3), Card(5, 2), Card(7, 3), Card(10, 1), Card(10, 0)],
                 [Card(1, 2), Card(1, 3), Card(2, 2), Card(2, 3), Card(5, 2), Card(10, 1), Card(10, 0)],
                 [Card(1, 0), Card(2, 2), Card(2, 3), Card(5, 2), Card(9, 3), Card(10, 1), Card(10, 0)],
                 [Card(2, 1), Card(2, 2), Card(2, 3), Card(5, 2), Card(10, 3), Card(10, 1), Card(10, 0)],
                 [Card(2, 2), Card(2, 3), Card(5, 2), Card(10, 2), Card(10, 1), Card(10, 0), Card(12, 1)],
                 [Card(2, 2), Card(2, 3), Card(3, 1), Card(5, 2), Card(10, 1), Card(10, 0), Card(11, 1)]]
        cards_eval = [evaluate_cards(card) for card in cards]
        assert (cards_eval[0][0] == 2)
        assert (cards_eval[1][0] == 2)
        assert (cards_eval[2][0] == 2)
        assert (cards_eval[3][0] == 6)
        assert (cards_eval[4][0] == 6)
        assert (cards_eval[5][0] == 2)
        winning_indexes = decide_on_victory(cards_eval)
        assert (winning_indexes[0] == 3)
        assert (winning_indexes[1] == 4)
        assert (len(winning_indexes) == 2)

    def testFullHousePairIndexError(self):
        cards = [[Card(0, 2), Card(0, 3), Card(0, 1), Card(1, 2), Card(4, 3), Card(9, 2), Card(10, 3)],
                 [Card(0, 2), Card(0, 3), Card(0, 1), Card(1, 0), Card(1, 2), Card(9, 0), Card(9, 2)],
                 [Card(0, 2), Card(0, 3), Card(0, 1), Card(1, 2), Card(9, 1), Card(9, 2), Card(12, 0)],
                 [Card(0, 2), Card(0, 3), Card(0, 1), Card(1, 2), Card(5, 3), Card(6, 3), Card(9, 2)],
                 [Card(0, 2), Card(0, 3), Card(0, 1), Card(1, 2), Card(6, 1), Card(9, 2), Card(11, 0)],
                 [Card(0, 2), Card(0, 3), Card(0, 1), Card(1, 3), Card(1, 2), Card(5, 1), Card(9, 2)]]

        cards_eval = [evaluate_cards(card) for card in cards]
        assert (cards_eval[0][0] == 3)
        assert (cards_eval[1][0] == 6)
        assert (cards_eval[2][0] == 6)
        assert (cards_eval[3][0] == 3)
        assert (cards_eval[4][0] == 3)
        assert (cards_eval[5][0] == 6)
        winning_indexes = decide_on_victory(cards_eval)
        assert (winning_indexes[0] == 1)
        assert (winning_indexes[1] == 2)
        assert (len(winning_indexes) == 2)

    def testTwoStraightsWithSameValueRange(self):
        cards = [
            [Card(3, 3), Card(5, 3), Card(6, 3), Card(8, 2), Card(10, 1), Card(11, 2), Card(12, 0)],
            [Card(5, 3), Card(6, 2), Card(8, 2), Card(10, 1), Card(11, 2), Card(12, 1), Card(12, 0)],
            [Card(0, 1), Card(5, 3), Card(7, 0), Card(8, 2), Card(10, 1), Card(11, 2), Card(12, 0)],
            [Card(5, 2), Card(5, 3), Card(8, 2), Card(9, 3), Card(10, 1), Card(11, 2), Card(12, 0)],
            [Card(2, 3), Card(5, 3), Card(8, 3), Card(8, 2), Card(10, 1), Card(11, 2), Card(12, 0)],
            [Card(4, 2), Card(5, 3), Card(8, 2), Card(9, 2), Card(10, 1), Card(11, 2), Card(12, 0)]]

        cards_eval = [evaluate_cards(card) for card in cards]
        assert (cards_eval[0][0] == 0)
        assert (cards_eval[1][0] == 1)
        assert (cards_eval[2][0] == 0)
        assert (cards_eval[3][0] == 4)
        assert (cards_eval[4][0] == 1)
        assert (cards_eval[5][0] == 4)
        winning_indexes = decide_on_victory(cards_eval)
        assert (winning_indexes[0] == 3)
        assert (winning_indexes[1] == 5)
        assert (len(winning_indexes) == 2)

    def testNoWinnerAllPairs(self):
        cards = [
            [Card(3, 1), Card(4, 3), Card(6, 0), Card(7, 2), Card(10, 1), Card(12, 2), Card(12, 3)],
            [Card(2, 2), Card(3, 1), Card(4, 1), Card(4, 3), Card(6, 0), Card(7, 2), Card(12, 3)],
            [Card(1, 3), Card(3, 1), Card(4, 3), Card(6, 0), Card(7, 3), Card(7, 2), Card(12, 3)],
            [Card(1, 0), Card(3, 1), Card(4, 2), Card(4, 3), Card(6, 0), Card(7, 2), Card(12, 3)],
            [Card(3, 1), Card(4, 3), Card(6, 0), Card(7, 0), Card(7, 2), Card(9, 1), Card(12, 3)],
            [Card(0, 0), Card(3, 1), Card(4, 3), Card(6, 0), Card(7, 2), Card(12, 1), Card(12, 3)]]
        cards_eval = [evaluate_cards(card) for card in cards]
        assert (cards_eval[0][0] == 1)
        assert (cards_eval[1][0] == 1)
        assert (cards_eval[2][0] == 1)
        assert (cards_eval[3][0] == 1)
        assert (cards_eval[4][0] == 1)
        assert (cards_eval[5][0] == 1)
        winning_indexes = decide_on_victory(cards_eval)
        assert (winning_indexes[0] == 0)
        assert (len(winning_indexes) == 1)

    def testStraightWithPair(self):
        cards = [
            [Card(3, 1), Card(5, 3), Card(6, 0), Card(7, 1), Card(8, 3), Card(8, 0), Card(9, 3)],
            [Card(0, 0), Card(3, 1), Card(6, 1), Card(6, 0), Card(8, 3), Card(8, 0), Card(9, 3)],
            [Card(3, 1), Card(6, 0), Card(8, 3), Card(8, 0), Card(9, 3), Card(10, 2), Card(12, 1)],
            [Card(1, 2), Card(3, 1), Card(5, 3), Card(6, 0), Card(8, 3), Card(8, 0), Card(9, 3)],
            [Card(3, 1), Card(4, 0), Card(6, 0), Card(8, 3), Card(8, 0), Card(9, 3), Card(11, 2)],
            [Card(3, 1), Card(4, 2), Card(6, 3), Card(6, 0), Card(8, 3), Card(8, 0), Card(9, 3)]]
        cards_eval = [evaluate_cards(card) for card in cards]
        assert (cards_eval[0][0] == 4)
        assert (cards_eval[1][0] == 2)
        assert (cards_eval[2][0] == 1)
        assert (cards_eval[3][0] == 1)
        assert (cards_eval[4][0] == 1)
        assert (cards_eval[5][0] == 2)
        winning_indexes = decide_on_victory(cards_eval)
        assert (winning_indexes[0] == 0)
        assert (len(winning_indexes) == 1)

    def testFullHouseHigherPairLoses(self):
        cards = [
            [Card(0, 3), Card(12, 1), Card(3, 2), Card(5, 1), Card(5, 2), Card(5, 3), Card(12, 0)],
            [Card(0, 3), Card(0, 1), Card(3, 2), Card(6, 1), Card(6, 2), Card(6, 3), Card(12, 0)],
            [Card(0, 3), Card(0, 1), Card(3, 2), Card(6, 1), Card(6, 2), Card(6, 3), Card(12, 0)]]
        cards_eval = [evaluate_cards(card) for card in cards]
        assert (cards_eval[0][0] == 6)
        assert (cards_eval[1][0] == 6)
        assert (cards_eval[2][0] == 6)
        winning_indexes = decide_on_victory(cards_eval)
        assert (winning_indexes[0] == 1)
        assert (winning_indexes[1] == 2)
        assert (len(winning_indexes) == 2)

    def testFullHouseHigherPair(self):
        cards = [
            [Card(0, 3), Card(12, 1), Card(3, 2), Card(6, 1), Card(6, 2), Card(6, 3), Card(12, 0)],
            [Card(0, 3), Card(0, 1), Card(3, 2), Card(6, 1), Card(6, 2), Card(6, 3), Card(12, 0)]]
        cards_eval = [evaluate_cards(card) for card in cards]
        assert (cards_eval[0][0] == 6)
        assert (cards_eval[1][0] == 6)
        winning_indexes = decide_on_victory(cards_eval)
        assert (winning_indexes[0] == 0)
        assert (len(winning_indexes) == 1)

    def testEqualFullHouse(self):
        cards = [
            [Card(0, 3), Card(0, 1), Card(3, 2), Card(6, 1), Card(6, 2), Card(6, 3), Card(12, 0)],
            [Card(0, 3), Card(0, 1), Card(3, 2), Card(6, 1), Card(6, 2), Card(6, 3), Card(12, 0)]]
        cards_eval = [evaluate_cards(card) for card in cards]
        assert (cards_eval[0][0] == 6)
        assert (cards_eval[1][0] == 6)
        winning_indexes = decide_on_victory(cards_eval)
        assert (winning_indexes[0] == 0)
        assert (winning_indexes[1] == 1)
        assert (len(winning_indexes) == 2)

    def testCrashFullHouse(self):
        cards = [
            [Card(0, 3), Card(0, 1), Card(3, 2), Card(6, 2), Card(6, 3), Card(8, 1), Card(9, 2)],
            [Card(0, 3), Card(0, 1), Card(2, 1), Card(3, 2), Card(6, 2), Card(6, 3), Card(11, 2)],
            [Card(0, 3), Card(0, 1), Card(1, 0), Card(3, 2), Card(6, 2), Card(6, 3), Card(7, 0)],
            [Card(0, 0), Card(0, 3), Card(0, 1), Card(3, 3), Card(3, 2), Card(6, 2), Card(6, 3)],
            [Card(0, 3), Card(0, 1), Card(3, 2), Card(6, 1), Card(6, 2), Card(6, 3), Card(12, 0)],
            [Card(0, 3), Card(0, 1), Card(3, 2), Card(4, 0), Card(6, 2), Card(6, 3), Card(12, 1)]]
        cards_eval = [evaluate_cards(card) for card in cards]
        assert (cards_eval[0][0] == 2)
        assert (cards_eval[1][0] == 2)
        assert (cards_eval[2][0] == 2)
        assert (cards_eval[3][0] == 6)
        assert (cards_eval[4][0] == 6)
        assert (cards_eval[5][0] == 2)
        winning_indexes = decide_on_victory(cards_eval)
        assert (winning_indexes[0] == 4)
        assert (len(winning_indexes) == 1)

    def testWrongTwoPairChosen(self):
        cards = [
            [Card(1, 3), Card(3, 1), Card(3, 0), Card(4, 3), Card(5, 1), Card(10, 1), Card(10, 3)],
            [Card(1, 3), Card(2, 2), Card(3, 0), Card(4, 3), Card(7, 1), Card(10, 1), Card(10, 3)],
            [Card(1, 3), Card(3, 0), Card(4, 3), Card(6, 2), Card(8, 3), Card(10, 1), Card(10, 3)],
            [Card(1, 0), Card(1, 3), Card(3, 0), Card(4, 3), Card(7, 2), Card(10, 1), Card(10, 3)],
            [Card(1, 3), Card(3, 0), Card(4, 3), Card(8, 1), Card(10, 1), Card(10, 3), Card(11, 3)],
            [Card(1, 1), Card(1, 3), Card(3, 0), Card(4, 3), Card(9, 2), Card(10, 1), Card(10, 3)]]
        cards_eval = [evaluate_cards(card) for card in cards]
        assert (cards_eval[0][0] == 2)
        assert (cards_eval[1][0] == 1)
        assert (cards_eval[2][0] == 1)
        assert (cards_eval[3][0] == 2)
        assert (cards_eval[4][0] == 1)
        assert (cards_eval[5][0] == 2)
        winning_indexes = decide_on_victory(cards_eval)
        assert (winning_indexes[0] == 0)
        assert (len(winning_indexes) == 1)

    def testStraightFlushAceHigh(self):
        cards = [
            [Card(12, 1), Card(0, 1), Card(1, 1), Card(2, 1), Card(3, 1), Card(9, 1), Card(6, 1)],
            [Card(0, 1), Card(2, 1), Card(3, 1), Card(1, 1), Card(11, 1), Card(4, 1), Card(7, 1)]]
        cards_eval = [evaluate_cards(card) for card in cards]
        assert(cards_eval[0][0] == 8)
        assert (cards_eval[1][0] == 8)
        winning_indexes = decide_on_victory(cards_eval)
        assert(winning_indexes[0] == 1)
        assert (len(winning_indexes) == 1)

    def testFlushException(self):
        cards = [
            [Card(0, 1), Card(0, 3), Card(1, 3), Card(2, 3), Card(3, 3), Card(5, 3), Card(6, 0)],
            [Card(0, 3), Card(2, 3), Card(3, 2), Card(3, 3), Card(5, 3), Card(6, 2), Card(6, 0)],
            [Card(0, 3), Card(2, 3), Card(3, 3), Card(5, 3), Card(6, 3), Card(6, 0), Card(12, 2)],
            [Card(0, 3), Card(2, 3), Card(3, 3), Card(5, 3), Card(6, 0), Card(8, 1), Card(9, 1)],
            [Card(0, 3), Card(2, 3), Card(3, 3), Card(4, 3), Card(5, 3), Card(6, 0), Card(11, 0)],
            [Card(0, 0), Card(0, 3), Card(2, 3), Card(3, 3), Card(5, 3), Card(6, 0), Card(9, 0)]]
        cards_eval = [evaluate_cards(card) for card in cards]
        winning_indexes = decide_on_victory(cards_eval)
        assert(winning_indexes[0] == 2)
        assert (len(winning_indexes) == 1)

    def testStraightAceHigh(self):
        cards = [
            [Card(12, 1), Card(0, 0), Card(1, 1), Card(2, 3), Card(3, 3), Card(9, 3), Card(6, 0)],
            [Card(0, 3), Card(2, 3), Card(3, 2), Card(1, 0), Card(11, 3), Card(4, 2), Card(7, 0)]]
        cards_eval = [evaluate_cards(card) for card in cards]
        assert(cards_eval[0][0] == 4)
        assert (cards_eval[1][0] == 4)
        winning_indexes = decide_on_victory(cards_eval)
        assert(winning_indexes[0] == 1)
        assert (len(winning_indexes) == 1)
