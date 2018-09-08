from pokerlib.domain import Game
from pokerlib.Evalutaor import evaluate_cards
from pokerlib.DecisionMaker import decide_on_victory
from pokerlib.visualize import debug_play

NUM_PLAYERS = 6
for i in range(1000):
    game = Game(num_players=NUM_PLAYERS)
    cards = [game.get_showdown_cards_of_player(i)for i in range(NUM_PLAYERS)]
    cards_eval = [evaluate_cards(card) for card in cards]
    print("cards: ", cards)
    winning_indexes = decide_on_victory(cards_eval)
    #log = "Cards: " + str(cards) + "\n"
    #log += "Eval: " + str(cards_eval) + "\n"
    #log += "Winners: " + str([cards[index] for index in winning_indexes])
    #print(log)
    #debug_play(game, winning_indexes, log)



