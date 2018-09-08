import unittest
from pokerlib.Evalutaor import evaluate_cards
from pokerlib import Evalutaor
from pokerlib.domain import Card

HAND_ROYAL_FLUSH = [Card(11, 0), Card(12, 0), Card(8, 0), Card(9, 0),
                    Card(2, 1), Card(10, 0), Card(5, 2)]
HAND_STRAIGHT_FLUSH = [Card(7, 3), Card(11, 0), Card(10, 0), Card(9, 0),
                       Card(8, 0), Card(2, 1), Card(7, 0)]
HAND_QUADS = [Card(1, 0), Card(7, 1), Card(10, 0), Card(7, 3),
              Card(8, 0), Card(7, 2), Card(7, 0)]
HAND_FULL_HOUSE = [Card(1, 0), Card(8, 1), Card(10, 0), Card(7, 3),
                   Card(8, 0), Card(7, 2), Card(7, 0)]
HAND_FLUSH = [Card(1, 1), Card(4, 0), Card(10, 0), Card(7, 3),
              Card(8, 0), Card(7, 0), Card(6, 0)]
HAND_STRAIGHT = [Card(1, 0), Card(2, 1), Card(10, 0), Card(4, 3),
                 Card(8, 0), Card(3, 2), Card(5, 0)]
HAND_TRIPS = [Card(1, 0), Card(3, 1), Card(10, 0), Card(7, 3),
              Card(8, 0), Card(7, 2), Card(7, 1)]
HAND_TWO_PAIR = [Card(1, 0), Card(8, 1), Card(10, 0), Card(7, 3),
                 Card(8, 0), Card(7, 2), Card(3, 0)]
HAND_PAIR = [Card(1, 0), Card(8, 1), Card(10, 1), Card(12, 3),
             Card(8, 0), Card(7, 2), Card(4, 0)]
HAND_HIGH_CARD = [Card(1, 0), Card(2, 1), Card(10, 1), Card(12, 3),
                  Card(8, 0), Card(7, 2), Card(4, 0)]


class TestEvaluator(unittest.TestCase):

    def test_yet_another_hand_that_wants_to_be_a_royal_flush_but_is_a_flush(self):
        hand = [Card(0, 2), Card(4, 3), Card(8, 3), Card(9, 2), Card(10, 2), Card(11, 2), Card(12, 2)]
        val = evaluate_cards(hand)
        self.assertEqual(val[0], Evalutaor.FLUSH)

    def test_another_hand_that_wants_to_be_a_royal_flush_but_is_a_flush(self):
        hand = [Card(0, 2), Card(7, 1), Card(8, 3), Card(9, 1), Card(10, 1), Card(11, 1), Card(12, 1)]
        val = evaluate_cards(hand)
        self.assertEqual(val[0], Evalutaor.FLUSH)


    def test_hand_that_wants_to_be_a_royal_flush_but_is_a_flush(self):
        hand = [Card(0, 2), Card(1, 2), Card(8, 2), Card(9, 3), Card(10, 1), Card(11, 2), Card(12, 2)]
        val = evaluate_cards(hand)
        self.assertEqual(val[0], Evalutaor.FLUSH)

    def test_royal_flush(self):
        val = evaluate_cards(HAND_ROYAL_FLUSH)
        self.assertEqual(val[0], Evalutaor.ROYAL_FLUSH)

    def test_straight_flush(self):
        val = evaluate_cards(HAND_STRAIGHT_FLUSH)
        self.assertEqual(val[0], Evalutaor.STRAIGHT_FLUSH)

    def test_quads(self):
        val = evaluate_cards(HAND_QUADS)
        self.assertEqual(val[0], Evalutaor.FOUR_OF_A_KIND)

    def test_full_house(self):
        val = evaluate_cards(HAND_FULL_HOUSE)
        self.assertEqual(val[0], Evalutaor.FULL_HOUSE)

    def test_flush(self):
        val = evaluate_cards(HAND_FLUSH)
        self.assertEqual(val[0], Evalutaor.FLUSH)

    def test_straight(self):
        val = evaluate_cards(HAND_STRAIGHT)
        self.assertEqual(val[0], Evalutaor.STRAIGHT)

    def test_trips(self):
        val = evaluate_cards(HAND_TRIPS)
        self.assertEqual(val[0], Evalutaor.THREE_OF_A_KIND)

    def test_two_pair(self):
        val = evaluate_cards(HAND_TWO_PAIR)
        self.assertEqual(val[0], Evalutaor.TWO_PAIR)

    def test_pair(self):
        val = evaluate_cards(HAND_PAIR)
        self.assertEqual(val[0], Evalutaor.PAIR)

    def test_high_card(self):
        val = evaluate_cards(HAND_HIGH_CARD)
        self.assertEqual(val[0], Evalutaor.HIGH_CARD)

if __name__ == '__main__':
    unittest.main()
