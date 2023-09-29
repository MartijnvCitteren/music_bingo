from scraps import read_xlsx
import format_string

from tkinter import filedialog, simpledialog
import tkinter as tk
import random

############################################################################################

root = tk.Tk()
root.withdraw() # Hide the main window
root.call('wm', 'attributes', '.', '-topmost', True)

xlsx_path = filedialog.askopenfilename(title="Open Excel-bestand met titel en artiesten...", filetypes=[("Excel Files", "*.xlsx")])
print("Locatie Excelbestand:", xlsx_path)

jpg_path = filedialog.askopenfilename(title="Open JPG-bestand met de bingokaart...", filetypes=[("JPG Files", "*.jpg")])
print("Locatie JPG-bestand:", jpg_path)


root = tk.Tk()
root.withdraw() # Hide the main window
root.call('wm', 'attributes', '.', '-topmost', True)
no_cards = simpledialog.askinteger("Aantal bingokaarten", "Aantal bingokaarten:")
no_cards = int(no_cards)
print("Aantal bingokaarten:", no_cards)


pdf_path = filedialog.asksaveasfilename(title="Sla het PDF-bestand op als...", filetypes=[("PDF Files", "*.pdf")], defaultextension=".pdf")

# converting the uploaded xlsx file to a (merged) list with all the songs and artists.
songs_and_artist = read_xlsx.xlsx_to_list(xlsx_path)

# while loop for creating X bingo cards TO DO
# right now just testing with 1 bingo card
card_size = 9
bingocard = (random.sample(songs_and_artist, card_size))
#print(bingocard)
# i=index in de latere while loop

j = 0
for song in bingocard:
    artist, song = format_string.format_output(bingocard[j])
    j += 1
    print(artist)
    print(song)

# function that places each artist and song in the right place on the bingo card, without (in worst case scenario)
# we need to create (25 places to fill * 75 bingocards * 2(because 1 song, 1 artist =) 3.750 images that we need to
# merge later on.