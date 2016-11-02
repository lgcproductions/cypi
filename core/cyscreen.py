#!/usr/bin/python
#Screen file for Cypi.							#
#Easily add screen functions					#
#V1.0											#
#Thank's to all that have helped with this code	#
#################################################
import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI
import time
from PIL import Image, ImageDraw, ImageFont


#define pins for the display
DC = 25 		#5110
RST = 24		#5110
SPI_PORT = 0	#5110
SPI_DEVICE = 0	#5110

disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

# Software SPI usage (defaults to bit-bang SPI interface):
#disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)

# Initialize library.
disp.begin(contrast=60)

image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
 
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
 
# Draw a white filled box to clear the image.
draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)

# Clear display.
disp.clear()
disp.display()

#Get font
font = ImageFont.load_default()
draw = ImageDraw.Draw(image)


def screenLogo():
	# Load image and convert to 1 bit color.
	image = Image.open('cypi_logo.ppm').convert('1')

	# Alternatively load a different format image, resize it, and convert to 1 bit color.
	#image = Image.open('cypi_logo.png').resize((LCD.LCDWIDTH, LCD.LCDHEIGHT), Image.ANTIALIAS).convert('1')

	# Display image.
	disp.image(image)
	disp.display()
	
	
def screenWiierror():
	screenClear()
	draw.text((2,2), 'Cant connect', font=font)
	disp.image(image)
	disp.display() 

def screenWiiconnect():
	screenClear()
	draw.text((2,2), 'Press 1 + 2', font=font)
	disp.image(image)
	disp.display()

def screenConnected():
	screenClear()
	draw.text((2,2), 'Connected', font=font)
	disp.image(image)
	disp.display()
	
def screenClear():
	draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
	disp.clear()
	disp.display()
	
