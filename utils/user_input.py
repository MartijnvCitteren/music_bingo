from tkinter import simpledialog, filedialog
import tkinter as tk


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

def get_user_input():
    xlsx_path = get_file_path("Open Excel-bestand met titel en artiesten...", [("Excel Files", "*.xlsx")])
    print("Locatie Excelbestand:", xlsx_path)

    jpg_path = get_file_path("Open JPG-bestand met de bingokaart...", [("JPG Files", "*.jpg")])
    print("Locatie JPG-bestand:", jpg_path)

    n_cards = get_integer_input("Aantal bingokaarten:", "Aantal bingokaarten")
    print("Aantal bingokaarten:", n_cards)

    pdf_path = filedialog.asksaveasfilename(title="Sla het PDF-bestand op als...", filetypes=[("PDF Files", "*.pdf")], defaultextension=".pdf")

    return xlsx_path, jpg_path, n_cards, pdf_path