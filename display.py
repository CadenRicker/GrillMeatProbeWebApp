import time
import subprocess

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

class display:
    def __init__(self) -> None:
        # Create the I2C interface.
        self.i2c = busio.I2C(SCL, SDA)
        self.disp  = adafruit_ssd1306.SSD1306_I2C(128, 64, self.i2c, addr=0x3C)
        self.disp2 = adafruit_ssd1306.SSD1306_I2C(128, 64, self.i2c, addr=0X3D)
        # Clear display.
        self.disp.fill(0)
        self.disp.show()
        self.disp2.fill(0)
        self.disp2.show()
        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.
        self.width = self.disp.width
        self.height = self.disp.height
        self.image = Image.new("1", (self.width, self.height))
        self.image2 = Image.new("1", (self.width, self.height))
        # Get drawing object to draw on image.
        self.draw = ImageDraw.Draw(self.image)
        self.draw2 = ImageDraw.Draw(self.image2)
        # Draw a black filled box to clear the image.
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
        self.draw2.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
        # Draw some shapes.
        # First define some constants to allow easy resizing of shapes.
        padding = -2
        self.top = padding
        self.bottom = self.height - padding
        # Move left to right keeping track of the current x position for drawing shapes.
        self.x = 0


        # Load default font.
        #font = ImageFont.load_default()

        # Alternatively load a TTF font.  Make sure the .ttf font file is in the
        # same directory as the python script!
        # Some other nice fonts to try: http://www.dafont.com/bitmap.php
        self.fontTitle = ImageFont.truetype('upheavtt.ttf', 20)
        self.fontNumber = ImageFont.truetype('upheavtt.ttf', 46)
    def drawDisplay(self, displayValue1, displayValue2):
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
        self.draw2.rectangle((0, 0, self.width, self.height), outline=0, fill=0)


        self.draw.text((self.x, self.top + 0), "Probe 1", font=self.fontTitle, fill=255)
        self.draw.text((self.x, self.top + 24), "{:>3}°F".format(displayValue1,) , font=self.fontNumber, fill=255)
        self.draw2.text((self.x, self.top + 0), "Probe 2", font=self.fontTitle, fill=255)
        self.draw2.text((self.x, self.top + 24), "{:>3}°F".format(displayValue2,+1) , font=self.fontNumber, fill=255)

        # Display image.
        self.disp.image(self.image)
        self.disp.show()
        self.disp2.image(self.image2)
        self.disp2.show()
