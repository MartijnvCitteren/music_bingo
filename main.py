from utils import (user_input,
                   read_xlsx as read_file,
                   get_bingo_card_values as get_bingo,
                   print_bingo_card_image as print_card,
                   create_pdf as pdf)

def main():
    xlsx_path, jpg_path, n_cards, pdf_path = user_input.get_user_input()
    card_size = 9 #in a later stage we can ask users if they want 9, 16, 25 squares per bingo_card. for now it's fixxed
    songs_and_artists = read_file.xlsx_to_list(xlsx_path)

    image_paths = []
    for n in range(n_cards):
        bingocard = get_bingo.get_bingo_values(songs_and_artists, card_size)
        image_paths.append(print_card.make_bingo_card_9(bingocard, jpg_path))

    pdf.create_pdf(image_paths, pdf_path)
    pdf.remove_temp_images(image_paths)

    print("Het eindresultaat staat in:", pdf_path)





if __name__ == "__main__":
    main()