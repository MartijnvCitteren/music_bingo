from tkinter import simpledialog, filedialog, Tk

def create_root_window():
    root = Tk()
    root.withdraw()
    root.call('wm', 'attributes', '.', '-topmost', True)
    return root

def get_file_path(title, filetypes):
    root = create_root_window()
    file_path = filedialog.askopenfilename(title=title, filetypes=filetypes)
    root.destroy()  # Close the root window after use
    return file_path

def get_integer_input(prompt, title):
    root = create_root_window()
    value = simpledialog.askinteger(title, prompt)
    root.destroy()  # Close the root window after use
    return value

def get_user_input():
    xlsx_path = get_file_path("Open Excel-bestand met titel en artiesten...", [("Excel Files", "*.xlsx")])
    print("Locatie Excelbestand:", xlsx_path)

    jpg_path = get_file_path("Open JPG-bestand met de bingokaart...", [("JPG Files", "*.jpg")])
    print("Locatie JPG-bestand:", jpg_path)

    num_cards = get_integer_input("Aantal bingokaarten:", "Aantal bingokaarten")
    print("Aantal bingokaarten:", num_cards)

    pdf_path = filedialog.asksaveasfilename(title="Sla het PDF-bestand op als...", filetypes=[("PDF Files", "*.pdf")], defaultextension=".pdf")

    return xlsx_path, jpg_path, num_cards, pdf_path
