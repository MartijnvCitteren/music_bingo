from utils import (user_input,
                   print_bingo_card_image as print_card,
                   create_pdf as pdf)
import pandas as pd

def main():
    xlsx_path, jpg_path, num_cards, pdf_path = user_input.get_user_input()
    df_all = pd.read_excel(xlsx_path, names=['title', 'artist'])
    card_size = 9 # For now hardcoded, 3x3 bingo card
    
    image_paths = []
    for n in range(num_cards):
        df_sample = df_all.sample(card_size).reset_index() # Randomly select 5 title+artist pairs, and reset index
        image_path = print_card.make_bingo_card(jpg_path, df_sample)
        image_paths.append(image_path)

    pdf.create_pdf(image_paths, pdf_path)
    pdf.remove_temp_images(image_paths)

    print("Het eindresultaat staat in:", pdf_path)

if __name__ == "__main__":
    main()
