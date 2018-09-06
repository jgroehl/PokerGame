import matplotlib.image as image
import matplotlib.pylab as plt
import time as time
from scipy.ndimage import zoom

def debug_play(game, winning_indexes, log):
    TABLE_OFFSET = 220
    TIME_STAMP = str(time.time())
    plt.figure(figsize=(13, 8))
    im = image.imread("img/table.png")
    plt.figimage(im, xo=TABLE_OFFSET, yo=TABLE_OFFSET)
    flop = game.flop
    index = 0
    for card in flop:
        im = image.imread("cards/" + card.get_card_string())
        im = zoom(im, (0.2, 0.2, 1), order=0)
        plt.figimage(im, xo=TABLE_OFFSET + 150 + 110 * index, yo=TABLE_OFFSET + 130)
        index += 1
    im = image.imread("cards/" + game.turn.get_card_string())
    im = zoom(im, (0.2, 0.2, 1), order=0)
    plt.figimage(im, xo=TABLE_OFFSET + 150 + 110 * index, yo=TABLE_OFFSET + 130)
    index += 1
    im = image.imread("cards/" + game.river.get_card_string())
    im = zoom(im, (0.2, 0.2, 1), order=0)
    plt.figimage(im, xo=TABLE_OFFSET + 150 + 110 * index, yo=TABLE_OFFSET + 130)
    index += 1

    player_offsets = [[20, TABLE_OFFSET + 130], [TABLE_OFFSET, TABLE_OFFSET + 400],
                      [TABLE_OFFSET + 600, TABLE_OFFSET + 400],
                      [TABLE_OFFSET, 70], [TABLE_OFFSET + 600, 70], [TABLE_OFFSET + 800, TABLE_OFFSET + 130]]
    player_index = 0
    for hole_cards in game.hole_cards:
        card_index = 0
        for card in hole_cards:
            im = image.imread("cards/" + card.get_card_string())
            im = zoom(im, (0.2, 0.2, 1), order=0)
            plt.figimage(im, xo=player_offsets[player_index][0] + 110 * card_index, yo=player_offsets[player_index][1])
            card_index = card_index + 1
        if player_index in winning_indexes:
            im = image.imread("img/border.png")
            plt.figimage(im, xo=player_offsets[player_index][0], yo=player_offsets[player_index][1])
        player_index = player_index + 1
    plt.savefig("save/image.png")
    plt.close()
    with open("save/log.txt", "w") as logfile:
        logfile.writelines(log)