from PIL import Image, ImageDraw, ImageFont
import tempfile
import textwrap

def get_text_size_in_pixels(font, text):
    bbox = font.getbbox(text)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    return text_width, text_height

def print_to_card(draw, x, y, text, font, up_or_down, wrap_width=15):
    text_wrapped = textwrap.wrap(text, width=wrap_width)
    if (len(text_wrapped) > 1) and up_or_down == 'up':
        text_wrapped = reversed(text_wrapped) # work from center up or down, so reverse to ['Kids','War','Cold']
    
    delta_y = 22
    for line in text_wrapped:
        if up_or_down == 'up':
            y = int(y - delta_y)
        else:
            y = int(y + delta_y)
        draw.text((x, y), line, fill="black", anchor="mm", font=font)
        delta_y += 8 # _, line_height = get_text_size_in_pixels(font, 'Height of a line with random text') 

def make_bingo_card(image_path, df, card_size=9):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("cour.ttf", 20)

    x_center = [170, 450, 720] # center-coordinate (x-axis) of each columnn
    y_center = [290, 525, 751] # center-coordinate (y-axis) of each row
    
    num_rows_cols = int(len(df) ** 0.5)
    for row in range(num_rows_cols):
        for col in range(num_rows_cols):
            index = row*3+col
            
            x = x_center[col]
            y = y_center[row]
            
            # print '-'
            draw.text((x, y), '-', fill="black", anchor="mm", font=font)
            
            # print artist and title
            print_to_card(draw, x, y, df['artist'][index], font, up_or_down='up')
            print_to_card(draw, x, y, df['title'][index], font, up_or_down='down')

    img_rotated = img.transpose(Image.ROTATE_90)

    # Save the modified image to a temporary file
    temp_file = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
    img_rotated.save(temp_file.name, "JPEG")
    temp_file.close()

    return temp_file.name
