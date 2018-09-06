import numpy as np
from pokerlib.EvaluationStateMachine import FlushStateDevice, \
    StraightStateDevice, CardValueStateDevice

ROYAL_FLUSH = 9
STRAIGHT_FLUSH = 8
FOUR_OF_A_KIND = 7
FULL_HOUSE = 6
FLUSH = 5
STRAIGHT = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
PAIR = 1
HIGH_CARD = 0


def evaluate_cards(cards):
    cards = np.asarray(cards)
    cards.sort()
    cards_values = np.asarray([cards[i].value for i in range(len(cards))])
    cards_value_diff = [cards[i+1].value-cards[i].value for i in range(len(cards)-1)]

    suits = np.asarray([cards[i].suit for i in range(len(cards))])
    suits_indexes = np.argsort(suits)
    suits.sort()
    cards_suit_diff = [suits[i + 1] - suits[i] for i in range(len(suits) - 1)]

    flush_state_machine = FlushStateDevice()
    straight_state_machine = StraightStateDevice()
    value_state_machine = CardValueStateDevice()

    if len(cards) is not 7:
        raise AssertionError("Need seven cards to evaluate")

    for index in range(len(cards_suit_diff)):
        flush_state_machine.on_event(cards_suit_diff[index], index)
    flush_card_indexes = suits_indexes[flush_state_machine.used_card_indices]
    is_flush = flush_state_machine.state.evaluate()

    for index in range(len(cards_value_diff)):
        straight_state_machine.on_event(cards_value_diff[index], index)
        value_state_machine.on_event(cards_value_diff[index], index)
    is_straight = straight_state_machine.state.evaluate()
    straight_indexes = straight_state_machine.used_card_indices

    if not is_straight and \
            (12 in cards_values and
             0 in cards_values and
             1 in cards_values and
             2 in cards_values and
             3 in cards_values):
        is_straight = True
        ace_straight_values = [12, 0, 1, 2, 3]
        straight_indexes = np.asarray([np.where(cards_values == ace_straight_values[i])[0][0]
                            for i in range(len(ace_straight_values))])

    value_result = value_state_machine.state.evaluate()
    value_indexes = value_state_machine.used_card_indices

    sf_indexes = np.intersect1d(flush_card_indexes, straight_indexes)
    high_cards = list(np.copy(cards))
    if is_flush and is_straight and len(sf_indexes) > 4:
        if (cards[sf_indexes][-1].value == 12 and
           cards[sf_indexes][-2].value == 11): # Add the king in here for the ace to five straight flush check.
            return [ROYAL_FLUSH, cards[sf_indexes]]
        if cards[sf_indexes][-1].value == 12:
            sf_indexes = list(sf_indexes)
            sf_indexes.insert(0, sf_indexes.pop(-1))
            sf_indexes = np.asarray(sf_indexes)
        return [STRAIGHT_FLUSH, cards[sf_indexes], []]

    if value_result == FOUR_OF_A_KIND:
        return_cards = cards[value_indexes][-4:]
        for card in return_cards:
            high_cards.remove(card)
        return [FOUR_OF_A_KIND, return_cards, get_high_cards(high_cards, 1)]

    if value_result == FULL_HOUSE:
        return_cards = cards[value_indexes]
        return [FULL_HOUSE, return_cards[:], []]

    if is_flush:
        return_cards = cards[flush_card_indexes]
        return [FLUSH, return_cards[-5:], []]

    if is_straight:
        return_cards = cards[straight_indexes]
        return [STRAIGHT, return_cards[-5:], []]

    if value_result == THREE_OF_A_KIND:
        for card in cards[value_indexes]:
            high_cards.remove(card)
        return [THREE_OF_A_KIND, cards[value_indexes], get_high_cards(high_cards, 2)]

    if value_result == TWO_PAIR:
        return_cards = cards[value_indexes][-4:]
        for card in return_cards:
            high_cards.remove(card)
        return [TWO_PAIR, return_cards, get_high_cards(high_cards, 1)]

    if value_result == PAIR:
        for card in cards[value_indexes]:
            high_cards.remove(card)
        return [PAIR, cards[value_indexes], get_high_cards(high_cards, 3)]

    return [HIGH_CARD, [], cards[2:]]


def get_high_cards(cards, number):
    if len(cards) < number:
        raise AssertionError("cannot get so many high cards")
    cards.sort()
    return cards[(-1*number):]
