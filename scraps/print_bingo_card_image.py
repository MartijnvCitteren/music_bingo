from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import tempfile
import os
import math

######################################################################################
## creating a copy of juliens-function to experiment


song_1 = "Hey ya"
artist_1 = "Out cast"
song_2 = "Wonder wall"
artist_2 = "Oasis"

def center_x_axis(string):
    pixels_removed_to_center = math.ceil((len(string)/2)*13.3) #13.3 pixels are use by fontsize 24 with arial
    return pixels_removed_to_center

def make_bingo_card_9_boxxes(song_1, artist_1, song_2, artist_2, image_path):
    image = Image.open(image_template_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 24)

    center_column_one = 165
    #center_coumn_two = 435
    #center_column_three = 707

    draw.text(((center_column_one - center_x_axis(song_1)), 280), song_1, fill="black", font=font)
    draw.text(((center_column_one - center_x_axis(artist_1)), 300), artist_1, fill="black", font=font)
    draw.text(((center_column_one - center_x_axis(song_2)), 515), song_2, fill="black", font=font)
    draw.text(((center_column_one - center_x_axis(artist_2)), 535), artist_2, fill="black", font=font)
    image_final = image # remove function.rotate(90) for better visablity

    # Save the modified image to a temporary file
    temp_file = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
    image_final.save(temp_file.name, "JPEG")
    temp_file.close()
    print(temp_file.name)
    return temp_file.name  # Return the path to the temporary image file

image_template_path = 'template.jpg'


make_bingo_card_9_boxxes(song_1, artist_1, song_2, artist_2, image_path=image_template_path )