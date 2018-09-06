import unittest
from pokerlib.Evalutaor import evaluate_cards
from pokerlib import Evalutaor
from pokerlib.domain import Card

HAND_ROYAL_FLUSH = [Card(0, 11), Card(0, 12), Card(0, 8), Card(0, 9),
                    Card(1, 2), Card(0, 10),Card(2, 5)]
HAND_STRAIGHT_FLUSH = [Card(3, 7), Card(0, 11), Card(0, 10), Card(0, 9),
                       Card(0, 8), Card(1, 2), Card(0, 7)]
HAND_QUADS = [Card(0, 1), Card(1, 7), Card(0, 10), Card(3, 7),
              Card(0, 8), Card(2, 7), Card(0, 7)]
HAND_FULL_HOUSE = [Card(0, 1), Card(1, 8), Card(0, 10), Card(3, 7),
                   Card(0, 8), Card(2, 7), Card(0, 7)]
HAND_FLUSH = [Card(1, 1), Card(0, 4), Card(0, 10), Card(3, 7),
              Card(0, 8), Card(0, 7), Card(0, 6)]
HAND_STRAIGHT = [Card(0, 1), Card(1, 2), Card(0, 10), Card(3, 4),
                 Card(0, 8), Card(2, 3), Card(0, 5)]
HAND_TRIPS = [Card(0, 1), Card(1, 3), Card(0, 10), Card(3, 7),
              Card(0, 8), Card(2, 7), Card(1, 7)]
HAND_TWO_PAIR = [Card(0, 1), Card(1, 8), Card(0, 10), Card(3, 7),
                 Card(0, 8), Card(2, 7), Card(0, 3)]
HAND_PAIR = [Card(0, 1), Card(1, 8), Card(1, 10), Card(3, 12),
             Card(0, 8), Card(2, 7), Card(0, 4)]
HAND_HIGH_CARD = [Card(0, 1), Card(1, 2), Card(1, 10), Card(3, 12),
                  Card(0, 8), Card(2, 7), Card(0, 4)]


class TestEvaluator(unittest.TestCase):

    def test_royal_flush(self):
        print("ROYAL_FLUSH")
        val = evaluate_cards(HAND_ROYAL_FLUSH)
        print(val)
        self.assertEqual(val[0], Evalutaor.ROYAL_FLUSH)

    def test_straight_flush(self):
        print("STRAIGHT_FLUSH")
        val = evaluate_cards(HAND_STRAIGHT_FLUSH)
        print(val)
        self.assertEqual(val[0], Evalutaor.STRAIGHT_FLUSH)

    def test_quads(self):
        print("FOUR_OF_A_KIND")
        val = evaluate_cards(HAND_QUADS)
        print(val)
        self.assertEqual(val[0], Evalutaor.FOUR_OF_A_KIND)

    def test_full_house(self):
        print("FULL_HOUSE")
        val=evaluate_cards(HAND_FULL_HOUSE)
        print(val)
        self.assertEqual(val[0], Evalutaor.FULL_HOUSE)

    def test_flush(self):
        print("FLUSH")
        val=evaluate_cards(HAND_FLUSH)
        print(val)
        self.assertEqual(val[0], Evalutaor.FLUSH)

    def test_straight(self):
        print("STRAIGHT")
        val = evaluate_cards(HAND_STRAIGHT)
        print(val)
        self.assertEqual(val[0], Evalutaor.STRAIGHT)

    def test_trips(self):
        print("THREE_OF_A_KIND")
        val = evaluate_cards(HAND_TRIPS)
        print(val)
        self.assertEqual(val[0], Evalutaor.THREE_OF_A_KIND)

    def test_two_pair(self):
        print("TWO_PAIR")
        val = evaluate_cards(HAND_TWO_PAIR)
        print(val)
        self.assertEqual(val[0], Evalutaor.TWO_PAIR)

    def test_pair(self):
        print("PAIR")
        val = evaluate_cards(HAND_PAIR)
        print(val)
        self.assertEqual(val[0], Evalutaor.PAIR)

    def test_high_card(self):
        print("HIGH_CARD")
        val = evaluate_cards(HAND_HIGH_CARD)
        print(val)
        self.assertEqual(val[0], Evalutaor.HIGH_CARD)

if __name__ == '__main__':
    unittest.main()
