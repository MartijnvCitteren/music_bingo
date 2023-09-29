from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import tempfile
import os


## creating a copy of juliens-function to experiment

song_1 = "Hey Ya"
artist_1 = "Out cast"
song_2 = "Wonder wall"
artist_2 = "Oasis"

x = 0
y = 0

def make_bingo_card_image(image_path, text=" ", x=x, y=y):
    image = Image.open(image_template_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 36)

    draw.text((x, y), text, fill="black", font=font)
    image_final = image.rotate(90)

    # Save the modified image to a temporary file
    temp_file = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
    image_final.save(temp_file.name, "JPEG")
    temp_file.close()

    return temp_file.name  # Return the path to the temporary image file

image_template_path = 'template.jpg'

    #for j in range(1, 9, 1):
j = 1
if j == 1:
    x = 15
    y = 15
    song = song_1
    artist = artist_1

else:
    x = 200
    y = 200

make_bingo_card_image(image_path=image_template_path,text=song, x=x, y=y)