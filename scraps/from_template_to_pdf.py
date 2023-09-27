
# import modules
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import tempfile
import os


# functions
def make_bingo_card_image(image_path, text="Hier had uw \n - \ntekst kunnen staan", x=550, y=420):
    image = Image.open(image_template_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 36)
        
    draw.text((x, y), text, fill="black", font=font)

    # Save the modified image to a temporary file
    temp_file = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
    image.save(temp_file.name, "JPEG")
    temp_file.close()
    
    return temp_file.name  # Return the path to the temporary image file

def create_pdf(image_paths, pdf_path):
    c = canvas.Canvas(pdf_path, pagesize=letter)

    # resize the figure to fit it on a page
    image = Image.open(image_paths[0])
    image_sz = image.size
    scale_factor = 0.7*letter[0]/image_sz[0]
    
    scaled_width = int(image_sz[0] * scale_factor)
    scaled_height = int(image_sz[1] * scale_factor)

    for i in range(0, len(image_paths)):
        if i % 2 == 0: # First card on a page (top)
            c.drawImage(image_paths[i], 50, 0.5*letter[1], width=scaled_width, height=scaled_height)
        else: # Second card on a page (bottom)
            c.drawImage(image_paths[i], 50, 75, width=scaled_width, height=scaled_height)
            c.showPage() # add page
    c.save()


# user input
no_cards = 5
image_template_path = 'template.jpg'
pdf_path = 'bingo_cards.pdf'

# create bingo cards 
image_paths = []
for i in range(0, no_cards):
    img_path = make_bingo_card_image(image_path=image_template_path, text="Kaart #"+str(i+1))
    image_paths.append(img_path)

create_pdf(image_paths, pdf_path)

# clean up temporary image files
for img_path in image_paths:
    os.remove(img_path)   
    
print("Het eindresultaat staat in:", pdf_path)
