import tkinter as tk
from tkinter import filedialog, simpledialog

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
no_cards = simpledialog.askfloat("Aantal bingokaarten", "Aantal bingokaarten:")
no_cards = int(no_cards)
print("Aantal bingokaarten:", no_cards)

# or via input() (probably less clear that user input is needed to continue)

user_input = input("Aantal bingokaarten: ")
no_cards = int(no_cards)
print("Aantal bingokaarten:", user_input)

pdf_path = filedialog.asksaveasfilename(title="Sla het PDF-bestand op als...", filetypes=[("PDF Files", "*.pdf")], defaultextension=".pdf")
