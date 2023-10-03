from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import tempfile
import os

######################################################################################
"""
STEP-BY-STEP LOGIC for filling 1 square
1. Input is 2 variables (song & artist)
2. Define y-as for SONG. For example y-as = 100_chars - len(song)
3. print var_song on (x: 200, y: above defined Y-axis)
4. define y-as for ARTIST. For example y-as = 100_chars - len(artist)
5 print var_artist on (x: 220, y: above defined Y-axis)
6. +1 counter index. 

Next step would be to get the next Song and Artist and repeat the above steps. 

After these steps - save the image... 

Seems complicated, research different possibilites.
"""





## creating a copy of juliens-function to experiment

song_1 = "Hey Ya"
artist_1 = "Out cast"
song_2 = "Wonder wall"
artist_2 = "Oasis"

x=0
y=0
index = 0

def make_bingo_card_9_image(image_path, text=" ", x=x, y=y, index=index):
    image = Image.open(image_template_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 36)

    draw.text((x, y), text, fill="black", font=font)
    image_final = image # remove function.rotate(90) for better visablity

    # Save the modified image to a temporary file
    temp_file = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
    image_final.save(temp_file.name, "JPEG")
    temp_file.close()
    print(temp_file.name)
    return temp_file.name  # Return the path to the temporary image file

image_template_path = 'template.jpg'

    #for j in range(1, 9, 1):
j = 1
if j == 1:
    x = 150
    y = 350
    song = song_1
    artist = artist_1

else:
    x = 200
    y = 200

make_bingo_card_image(image_path=image_template_path,text=song, x=x, y=y)