from PIL import Image, ImageDraw, ImageFont
import tempfile
import textwrap

def make_bingo_card(image_path, df, card_size=9):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("cour.ttf", 20)

    line_width,line_height = draw.textsize('-', font)
    x_center = [170, 450, 720] # center-coordinate (x-axis) of each columnn
    y_center = [290, 525, 751] # center-coordinate (y-axis) of each row
    char_max = 14 # max nr of characters

    num_rows_cols = int(len(df) ** 0.5)
    for row in range(num_rows_cols):
        for col in range(num_rows_cols):
            index = row*3+col
            
            x_cen = x_center[col]
            y_cen = y_center[row]
            
            # print artist
            artist_wrapped = textwrap.fill(df['artist'][index], width=char_max)
            text_width, text_height = draw.textsize(artist_wrapped, font)
            x = x_cen - text_width/2
            y = y_cen - 1.3*line_height - text_height
            draw.text((x, y), artist_wrapped, fill="black", font=font)
            
            # print '-'
            x = x_cen
            y = y_cen
            draw.text((x, y), '-', fill="black", font=font)
            
            # print title
            title_wrapped = textwrap.fill(df['title'][index], width=char_max)
            text_width, text_height = draw.textsize(title_wrapped, font)
            x = x_cen - text_width/2
            y = y_cen + 1.3*line_height
            draw.text((x, y), title_wrapped, fill="black", font=font)
            
    img_rotated = img.transpose(Image.ROTATE_90)

    # Save the modified image to a temporary file
    temp_file = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
    img_rotated.save(temp_file.name, "JPEG")
    temp_file.close()

    return temp_file.name
