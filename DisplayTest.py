# SPDX-FileCopyrightText: 2017 Tony DiCola for Adafruit Industries
# SPDX-FileCopyrightText: 2017 James DeVito for Adafruit Industries
# SPDX-License-Identifier: MIT

# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!

import time

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

i = 0
# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)
print(i2c.scan())
# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
disp  = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)
disp2 = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0X3D)
# Clear display.
disp.fill(0)
disp.show()
disp2.fill(0)
disp2.show()
# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new("1", (width, height))
image2 = Image.new("1", (width, height))
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
draw2 = ImageDraw.Draw(image2)
# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)
draw2.rectangle((0, 0, width, height), outline=0, fill=0)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
#font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
fontTitle = ImageFont.truetype('upheavtt.ttf', 20)
fontNumber = ImageFont.truetype('upheavtt.ttf', 46)
while True:

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw2.rectangle((0, 0, width, height), outline=0, fill=0)


    # Write four lines of text.
    if i <475:
        i +=1
    else:
        i = 0
    
    draw.text((x, top + 0), "Probe 1", font=fontTitle, fill=255)
    draw.text((x, top + 24), "{:>3}°F".format(i) , font=fontNumber, fill=255)
    draw2.text((x, top + 0), "Probe 2", font=fontTitle, fill=255)
    draw2.text((x, top + 24), "{:>3}°F".format(i+1) , font=fontNumber, fill=255)

    # Display image.
    disp.image(image)
    disp.show()
    disp2.image(image2)
    disp2.show()
    time.sleep(1)
