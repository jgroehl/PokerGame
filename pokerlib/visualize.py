import time as time
from PIL import Image, ImageDraw

def debug_play(game, winning_indexes, log):
    TABLE_OFFSET = 220
    CARD_SIZE = (180, 261)
    im = Image.new('RGBA', (1920, 1080), (75, 50, 25, 255))
    im_width, im_height = im.size

    tab = Image.open("img/table.png")
    tab_width, tab_height = tab.size
    ratio = 1300 / tab_width
    tab = tab.resize((int(tab_width*ratio), int(tab_height*ratio)), Image.ANTIALIAS)
    tab_width, tab_height = tab.size
    im.paste(tab, (int(im_width/2-tab_width/2), int(im_height/2-tab_height/2)), tab)
    flop = game.flop
    index = 0
    for card in flop:
        c = Image.open("cards/" + card.get_card_string())
        c = c.resize(CARD_SIZE, Image.ANTIALIAS)
        im.paste(c, (2*TABLE_OFFSET + 220 * index, int(1.8*TABLE_OFFSET)), c)
        index += 1
    c = Image.open("cards/" + game.turn.get_card_string())
    c = c.resize(CARD_SIZE, Image.ANTIALIAS)
    im.paste(c, (2 * TABLE_OFFSET + 220 * index, int(1.8 * TABLE_OFFSET)), c)    #plt.figimage(im, xo=TABLE_OFFSET + 150 + 110 * index, yo=TABLE_OFFSET + 130)
    index += 1
    c = Image.open("cards/" + game.river.get_card_string())
    c = c.resize(CARD_SIZE, Image.ANTIALIAS)
    im.paste(c, (2 * TABLE_OFFSET + 220 * index, int(1.8 * TABLE_OFFSET)), c)
    index += 1

    player_offsets = [[10, int(1.8 * TABLE_OFFSET)],
                      [TABLE_OFFSET, 60],
                      [TABLE_OFFSET + 400, 20],
                      [TABLE_OFFSET + 800, 20],
                      [TABLE_OFFSET + 1200, 60],
                      [TABLE_OFFSET + 1400, int(1.8 * TABLE_OFFSET)],
                      [TABLE_OFFSET, TABLE_OFFSET + 540],
                      [TABLE_OFFSET + 600, TABLE_OFFSET + 580],
                      [TABLE_OFFSET + 1200, TABLE_OFFSET + 540]]
    player_index = 0
    for hole_cards in game.hole_cards:
        card_index = 0
        for card in hole_cards:
            c = Image.open("cards/" + card.get_card_string())
            c = c.resize(CARD_SIZE, Image.ANTIALIAS)
            im.paste(c, (player_offsets[player_index][0] + 110 * card_index, player_offsets[player_index][1]), c)
            card_index = card_index + 1
        if player_index in winning_indexes:
            draw = ImageDraw.Draw(im)
            rx = player_offsets[player_index][0]
            ry = player_offsets[player_index][1]
            for i in range(-8, 1):
                draw.rectangle([(rx+i, ry+i), (rx+290-i, ry+260-i)], outline=(255, 0, 0, 255))
        player_index = player_index + 1
    im.save("save/image.png", "PNG")
    with open("save/log.txt", "w") as logfile:
        logfile.writelines(log)
