import random

#fictief aantal deelnemers voor POC
n_participants = 3

#fictieve afmeting bingo card - normaal tussen de 9(3*3) en 25(5*5)
card_size = 3

#voorbeeld lijst voor POC
song_and_artist = [["Carly Rae Jepsen", "Call Me Maybe"],
                   ["Lykke li", "I follow river"],
                   ["loreen", "Euphoria"],
                   ["Nielson", "Beauty & the brains"],
                   ["Jason Mraz", "I won't give up"],
                   ["Psy", "Gangnam Style"],
                   ["Train", "Drive By"],
                   ["Duncan Laurence", "Arcade"],
                   ["Suzan & Freek", "Blauwe Dag"]]


#============================================================

def random_bingo_vars(songs_and_artists,no_cards):
    card_size = 9
    n_bingocards = 0
    while n_bingocards < n_participants:
        bingocard = (random.sample(song_and_artist, card_size))
        n_bingocards += 1
        """
        if (card_size == 9):
            spot_1 = bingocard[0]
            spot_2 = bingocard[1]
            spot_3 = bingocard[2]
            spot_4 = bingocard[3]
            spot_5 = bingocard[4]
            spot_6 = bingocard[5]
            spot_7 = bingocard[6]
            spot_8 = bingocard[7]
            spot_9 = bingocard[8]

        else:
            print("INVALID CARD SIZE!")
    """
        #print(f"{bingocard[:card_size]} \n")


random_bingo_vars(song_and_artist,5)







