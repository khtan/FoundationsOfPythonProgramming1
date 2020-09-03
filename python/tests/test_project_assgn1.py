# region imports
import os
import sys
import logging
import pytest
import io
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
pytest.skip("skipping project_assgn1 tests, currently will show images and wait", allow_module_level=True) # currently using show to display pictures

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

# endregion tests
