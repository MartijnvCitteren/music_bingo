import random

card_size = 2
songs_and_artists =["laddie jee--hans Anders", "hoieldeeeeee--kees", "oelaalaaa--gerit", "boebadoeei--Annie"]

def get_bingo_values(songs_and_artists, card_size):
    bingocard = (random.sample(songs_and_artists, card_size))

    return bingocard
