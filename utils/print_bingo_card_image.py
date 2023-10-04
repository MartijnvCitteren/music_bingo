import math
from PIL import Image, ImageDraw, ImageFont
import tempfile
from math import ceil

def split_song(string):
    title = (str(string.split('--')[0]))
    return title
def split_artist(string):
    artist = (str(string.split('--')[1]))
    return artist

def px_removal_to_center(string):
    pixels_removed_to_center = math.ceil(((len(string)/2)*11.05)) #13 pixels are use by fontsize 20 with arial
    return pixels_removed_to_center

def make_bingo_card_9(bingocard, image_path):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 20)

    #creating variables // this might also be done in a loop? to-do
    song_1 = split_song(bingocard[0])
    song_2 = split_song(bingocard[1])
    song_3 = split_song(bingocard[2])
    song_4 = split_song(bingocard[3])
    song_5 = split_song(bingocard[4])
    song_6 = split_song(bingocard[5])
    song_7 = split_song(bingocard[6])
    song_8 = split_song(bingocard[7])
    song_9 = split_song(bingocard[8])

    artist_1 = split_artist(bingocard[0])
    artist_2 = split_artist(bingocard[1])
    artist_3 = split_artist(bingocard[2])
    artist_4 = split_artist(bingocard[3])
    artist_5 = split_artist(bingocard[4])
    artist_6 = split_artist(bingocard[5])
    artist_7 = split_artist(bingocard[6])
    artist_8 = split_artist(bingocard[7])
    artist_9 = split_artist(bingocard[8])

    #Defining the center (x-axis) op each columnn
    center_column_one = 170
    center_column_two = 450
    center_column_three = 720

    #Define the center (y-axis) of each row
    center_row_one = 290
    center_row_two = 525
    center_row_three = 751

    #spacing between rows in px
    spacing_rows = 12

    #printing text on the right spot
    draw.text(((center_column_one - px_removal_to_center(song_1)), (center_row_one - spacing_rows)), song_1, fill="black", font=font)
    draw.text(((center_column_one - px_removal_to_center(artist_1)), (center_row_one + spacing_rows)), artist_1, fill="black", font=font)
    draw.text(((center_column_one - px_removal_to_center(song_2)), (center_row_two - spacing_rows)), song_2, fill="black", font=font)
    draw.text(((center_column_one - px_removal_to_center(artist_2)), (center_row_two + spacing_rows)), artist_2, fill="black", font=font)
    draw.text(((center_column_one - px_removal_to_center(song_3)), (center_row_three - spacing_rows)), song_3, fill="black", font=font)
    draw.text(((center_column_one - px_removal_to_center(artist_3)), (center_row_three + spacing_rows)), artist_3, fill="black", font=font)

    draw.text(((center_column_two - px_removal_to_center(song_4)), center_row_one - spacing_rows), song_4, fill="black", font=font)
    draw.text(((center_column_two - px_removal_to_center(artist_4)), center_row_one + spacing_rows), artist_4, fill="black", font=font)
    draw.text(((center_column_two - px_removal_to_center(song_5)), (center_row_two - spacing_rows)), song_5, fill="black", font=font)
    draw.text(((center_column_two - px_removal_to_center(artist_5)), (center_row_two + spacing_rows)), artist_5, fill="black", font=font)
    draw.text(((center_column_two - px_removal_to_center(song_6)), (center_row_three - spacing_rows)), song_6, fill="black", font=font)
    draw.text(((center_column_two - px_removal_to_center(artist_6)), (center_row_three + spacing_rows)), artist_6, fill="black", font=font)

    draw.text(((center_column_three - px_removal_to_center(song_7)), center_row_one - spacing_rows), song_7, fill="black", font=font)
    draw.text(((center_column_three - px_removal_to_center(artist_7)), center_row_one + spacing_rows), artist_7, fill="black", font=font)
    draw.text(((center_column_three - px_removal_to_center(song_8)), (center_row_two - spacing_rows)), song_8, fill="black", font=font)
    draw.text(((center_column_three - px_removal_to_center(artist_8)), (center_row_two + spacing_rows)), artist_8, fill="black", font=font)
    draw.text(((center_column_three - px_removal_to_center(song_9)), (center_row_three - spacing_rows)), song_9, fill="black", font=font)
    draw.text(((center_column_three - px_removal_to_center(artist_9)), (center_row_three + spacing_rows)), artist_9, fill="black", font=font)

    image_rotated = image.rotate(90)

    # Save the modified image to a temporary file
    temp_file = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
    image_rotated.save(temp_file.name, "JPEG")
    temp_file.close()

    return temp_file.name