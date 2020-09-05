# region imports
import os
import sys
import logging
import pytest
import io
from enum import Enum
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import ImageDraw
from PIL import ImageFont

class Color(Enum):
    red = 0
    green = 1
    blue = 2

# pytest.skip("skipping project_assgn1 tests, currently will show images and wait", allow_module_level=True) # currently using show to display pictures

# from IPython.display import display
''' Notes
1. 
2.
'''
# from  pytest_mock import mocker
# endregion imports
# region globals
logger = logging.getLogger(__name__)
# endregion globals
# region helpers
# endregion helpers
# region tests for xx.x
def test_simple_show():
    file="..\data\msi_recruitment.gif"
    image=Image.open(file)
    image.show() # this works and holds the execution until display is closed
    # display(image) # this does not bring up any display
def test_blur():
    file="..\data\msi_recruitment.gif"
    image=Image.open(file)
    image = image.convert('RGB')
    blurred_image = image.filter(ImageFilter.BLUR)
    blurred_image.show()

def test_crop():
    file="..\data\msi_recruitment.gif"
    gif_image=Image.open(file)
    rgb_image=gif_image.convert('RGB')
    cropped = rgb_image.crop((50,0,190,150))
    cropped.show()

def test_draw_crop_box():
    file="..\data\msi_recruitment.gif"
    gif_image=Image.open(file)  # drawing on gif have poor rendering
    rgb_image=gif_image.convert('RGB')
    drawing_object = ImageDraw.Draw(rgb_image)
    drawing_object.rectangle((50,0,190,150), fill = None, outline = 'red')
    rgb_image.show()

def test_draw_text():
    file="..\data\msi_recruitment.gif"
    gif_image=Image.open(file)  # drawing on gif have poor rendering
    rgb_image=gif_image.convert('RGB')
    drawing_object = ImageDraw.Draw(rgb_image)
    drawing_object.text((50,0), "hello", fill = 'red', align = 'left')
    rgb_image.show()

def test_draw_text_with_font():
    file="..\data\msi_recruitment.gif"
    gif_image=Image.open(file)  # drawing on gif have poor rendering
    rgb_image=gif_image.convert('RGB')
    drawing_object = ImageDraw.Draw(rgb_image)
    font_object = ImageFont.truetype('../data/fanwood-webfont.ttf', 20)
    drawing_object.text((50,0), "hello world", fill = 'yellow', align = 'left', font = font_object)
    rgb_image.show()

def test_column_sheet_brightness():
    file="..\data\msi_recruitment.gif"
    gif_image=Image.open(file)
    rgb_image=gif_image.convert('RGB')
    enhancer = ImageEnhance.Brightness(rgb_image)
    images = []
    for i in range(0,10):
        images.append(enhancer.enhance(i/10))
    first_image = images[0]
    contact_sheet = Image.new(first_image.mode, (first_image.width, 10 * first_image.height))
    current_location = 0
    for img in images:
        contact_sheet.paste(img, (0, current_location))
        current_location = current_location + 450
    contact_sheet = contact_sheet.resize((160,900))
    contact_sheet.show()

def AddTextToImage(sourceImage, textLocation, textValue, fillValue, alignValue, fontObject):
    drawing = ImageDraw.Draw(sourceImage)
    drawing.text(textLocation, textValue, fill=fillValue, align=alignValue, font=fontObject)

def test_column_sheet_annotated_brightness():
    file="..\data\msi_recruitment.gif"
    gif_image=Image.open(file)
    rgb_image=gif_image.convert('RGB')
    enhancer = ImageEnhance.Brightness(rgb_image)
    images = []
    font_object = ImageFont.truetype('../data/fanwood-webfont.ttf', 40)
    for i in range(0,10):
        brightness = i/10;
        e_image = enhancer.enhance(brightness)
        AddTextToImage(e_image, (200,10), "brightness={}".format(brightness), 'black', 'left', font_object)
        images.append(e_image)
    first_image = images[0]
    contact_sheet = Image.new(first_image.mode, (first_image.width, 10 * first_image.height))
    current_location = 0
    for img in images:
        contact_sheet.paste(img, (0, current_location))
        current_location = current_location + 450
    contact_sheet = contact_sheet.resize((160,900))
    contact_sheet.show()
def test_grid_sheet_brightness():
    file="..\data\msi_recruitment.gif"
    gif_image=Image.open(file)
    rgb_image=gif_image.convert('RGB')
    enhancer = ImageEnhance.Brightness(rgb_image)
    images = []
    for i in range(0,10):
        images.append(enhancer.enhance(i/10))
    first_image = images[0]
    contact_sheet = Image.new(first_image.mode, (first_image.width *3, first_image.height *3))
    x=0
    y=0
    for img in images[1:]:
        contact_sheet.paste(img, (x, y))
        if x + first_image.width == contact_sheet.width:
            x = 0
            y = y + first_image.height
        else:
            x = x + first_image.width
    contact_sheet = contact_sheet.resize((int(contact_sheet.width/2), int(contact_sheet.height/2)))
    contact_sheet.show()

def test_grid_annotated_sheet_brightness():
    ''' 1. Annotation is added to the picture
        2. This is different from assignment where annotation is a small rectangle added to the picture
           This method might be better because it does not alter the original image
           However, the structure of processing images will have to change
    '''
    file="..\data\msi_recruitment.gif"
    gif_image=Image.open(file)
    (gif_width, gif_height) = gif_image.size
    logger.info("gheight={}".format(gif_height))
    gif_width = gif_image.width
    rgb_image=gif_image.convert('RGB')
    enhancer = ImageEnhance.Brightness(rgb_image)
    images = []
    font_object = ImageFont.truetype('../data/fanwood-webfont.ttf', 40)
    for i in range(0,10):
        brightness = i/10;
        e_image = enhancer.enhance(brightness)
        AddTextToImage(e_image, (int(gif_width * 0.1), int(gif_height * 0.9) ), "brightness={}".format(brightness), 'yellow', 'left', font_object)
        images.append(e_image)
    first_image = images[0]
    contact_sheet = Image.new(first_image.mode, (first_image.width *3, first_image.height *3))
    x=0
    y=0
    for img in images[1:]:
        contact_sheet.paste(img, (x, y))
        if x + first_image.width == contact_sheet.width:
            x = 0
            y = y + first_image.height
        else:
            x = x + first_image.width
    contact_sheet = contact_sheet.resize((int(contact_sheet.width/2), int(contact_sheet.height/2)))
    contact_sheet.show()

def test_grid_annotated_sheet_color():
    ''' 1. Full logic in loops
    '''
    file="..\data\msi_recruitment.gif"
    gif_image=Image.open(file)
    (gif_width, gif_height) = gif_image.size
    logger.info("gheight={}".format(gif_height))
    gif_width = gif_image.width
    rgb_image=gif_image.convert('RGB')
    R, G, B = 0, 1, 2
    images = []
    font_object = ImageFont.truetype('../data/fanwood-webfont.ttf', 40)
    for color in Color:
        for intensity in (0.1, 0.5, 0.9):
           bands = rgb_image.split()
           out = bands[color.value].point(lambda i: i * intensity )
           bands[color.value].paste(out, None)
           e_image = Image.merge('RGB', bands)
           AddTextToImage(e_image, (int(gif_width * 0.1), int(gif_height * 0.9) ), "c={} i={}".format(color, intensity), 'yellow', 'left', font_object)
           images.append(e_image)
    first_image = images[0]
    contact_sheet = Image.new(first_image.mode, (first_image.width *3, first_image.height *3))
    x=0
    y=0
    for img in images:
        contact_sheet.paste(img, (x, y))
        if x + first_image.width == contact_sheet.width:
            x = 0
            y = y + first_image.height
        else:
            x = x + first_image.width
    contact_sheet = contact_sheet.resize((int(contact_sheet.width/2), int(contact_sheet.height/2)))
    contact_sheet.show()

# endregion tests
