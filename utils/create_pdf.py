from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import tempfile
import os

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


# clean up temporary image files
def remove_temp_images(image_paths):
    for img_path in image_paths:
     os.remove(img_path)
