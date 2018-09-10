from pokerlib.domain import Game
from pokerlib.Evalutaor import evaluate_cards
from pokerlib.DecisionMaker import decide_on_victory
from pokerlib.visualize import debug_play
import time


NUM_PLAYERS = 9
NUM_HANDS = 100000
start = time.time()
for i in range(NUM_HANDS):
    game = Game(num_players=NUM_PLAYERS)
    cards = [game.get_showdown_cards_of_player(i)for i in range(NUM_PLAYERS)]
    try:
        cards_eval = [evaluate_cards(card) for card in cards]
        winning_indexes = decide_on_victory(cards_eval)
        if len(winning_indexes) == 0:
            raise Exception("no winner")
    except Exception as e:
        print("cards: ", cards)
        print(e)
    #log = "Cards: " + str(cards) + "\n"
    #log += "Eval: " + str(cards_eval) + "\n"
    #log += "Winners: " + str([cards[index] for index in winning_indexes])
    #print(log)
    #debug_play(game, winning_indexes, log)
end = time.time()
print(((end - start) / NUM_HANDS)*1000, "ms / hand")



