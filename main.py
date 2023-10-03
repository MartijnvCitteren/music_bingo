from tkinter import filedialog, simpledialog
import tkinter as tk
import random
from scraps import read_xlsx
import format_string

############################################################################################

def get_file_path(title, filetypes):
    root = tk.Tk()
    root.withdraw()
    root.call('wm', 'attributes', '.', '-topmost', True)
    file_path = filedialog.askopenfilename(title=title, filetypes=filetypes)
    return file_path

def get_integer_input(prompt, title):
    root = tk.Tk()
    root.withdraw()
    root.call('wm', 'attributes', '.', '-topmost', True)
    value = simpledialog.askinteger(title, prompt)
    return value

song_and_artist = []
def main():
    xlsx_path = get_file_path("Open Excel-bestand met titel en artiesten...", [("Excel Files", "*.xlsx")])
    print("Locatie Excelbestand:", xlsx_path)

    jpg_path = get_file_path("Open JPG-bestand met de bingokaart...", [("JPG Files", "*.jpg")])
    print("Locatie JPG-bestand:", jpg_path)

    no_cards = get_integer_input("Aantal bingokaarten:", "Aantal bingokaarten")
    print("Aantal bingokaarten:", no_cards)

    pdf_path = filedialog.asksaveasfilename(title="Sla het PDF-bestand op als...", filetypes=[("PDF Files", "*.pdf")], defaultextension=".pdf")

    songs_and_artists = read_xlsx.xlsx_to_list(xlsx_path)

    # while loop for creating X bingo cards TO DO
    # right now just testing with 1 bingo card
    card_size = 9
    bingocard = (random.sample(songs_and_artists, card_size))
    #print(bingocard)
    # i=index in de latere while loop

    index_j = 0
    for song in bingocard:
        artist, song = format_string.format_output(bingocard[j])
        index_j += 1
        print(artist)
        print(song)

# function that places each artist and song in the right place on the bingo card, without (in worst case scenario)
# we need to create (25 places to fill * 75 bingocards * 2(because 1 song, 1 artist =) 3.750 images that we need to
# merge later on.





if __name__ == "__main__":
    main()