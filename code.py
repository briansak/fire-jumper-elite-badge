''' 
Thank you for joining us at the 2HCY19 Security SEVT.  We thank you 
for your dedication and commitment to the Fire Jumper program. 

Enjoy the week and we please help us as we continue to evolve 
the Fire Jumper Elite program in the coming year!

--Brian and Lena

'''

# Circuit Playground Express CircuitPython Morse Code Flasher
# This is meant to work with the Circuit Playground Express board:
#   https://www.adafruit.com/product/3333
# Needs the NeoPixel module installed:
#   https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel
# Author: Collin Cunningham (modified by Brian Sak)
# License: MIT License (https://opensource.org/licenses/MIT)
 
import time
import random
 
import board
import neopixel
 
# Configuration:
# Message to display (capital letters and numbers only)
message = 'ELITE'
dot_length = 0.15  # Duration of one Morse dot
dash_length = (dot_length * 3.0)  # Duration of one Morse dash
symbol_gap = dot_length  # Duration of gap between dot or dash
character_gap = (dot_length * 3.0)  # Duration of gap between characters
flash_color = [(255,255,0),(255,0,0),(0,0,255),(192,192,192),(0,128,0),(255,0,255),(255,165,0),(0,255,255)]  # Selection of colors the neopixels can be. Randomly chosen later.
brightness = 0.5  # Display brightness (0.0 - 1.0)
morse = [
    ('A', '.-'),
    ('B', '-...'),
    ('C', '-.-.'),
    ('D', '-..'),
    ('E', '.'),
    ('F', '..-.'),
    ('G', '--.'),
    ('H', '....'),
    ('I', '..'),
    ('J', '.---'),
    ('K', '-.-'),
    ('L', '.-..'),
    ('M', '--'),
    ('N', '-.'),
    ('O', '---'),
    ('P', '.--.'),
    ('Q', '--.-'),
    ('R', '.-.'),
    ('S', '...'),
    ('T', '-'),
    ('U', '..-'),
    ('V', '...-'),
    ('W', '.--'),
    ('X', '-..-'),
    ('Y', '-.--'),
    ('Z', '--..'),
    ('0', '-----'),
    ('1', '.----'),
    ('2', '..---'),
    ('3', '...--'),
    ('4', '....-'),
    ('5', '.....'),
    ('6', '-....'),
    ('7', '--...'),
    ('8', '---..'),
    ('9', '----.'),
]
 
 
# Define a class that represents the morse flasher.
 
 
class MorseFlasher:
    def __init__(self, color):
        # set the color adjusted for brightness
        self._color = (
            int(color[0] * brightness),
            int(color[1] * brightness),
            int(color[2] * brightness)
        )
 
    def light(self, on=True):
        if on:
            pixels.fill(self._color)
        else:
            pixels.fill((0, 0, 0))
        pixels.show()
 
    def showDot(self):
        self.light(True)
        time.sleep(dot_length)
        self.light(False)
        time.sleep(symbol_gap)
 
    def showDash(self):
        self.light(True)
        time.sleep(dash_length)
        self.light(False)
        time.sleep(symbol_gap)
 
    def encode(self, string):
        output = ""
        # iterate through string's characters
        for c in string:
            # find morse code for a character
            for x in morse:
                if x[0] == c:
                    # add code to output
                    output += x[1]
            # add a space in between characters
            output += " "
        # save complete morse code output to display
        self.display(output)
 
    def display(self, code=".-.-.- "):
        # iterate through morse code symbols
        for c in code:
            # show a dot
            if c == ".":
                self.showDot()
            # show a dash
            elif c == "-":
                self.showDash()
            # show a gap
            elif c == " ":
                time.sleep(character_gap)
 
 
# Initialize NeoPixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)
pixels.fill((0, 0, 0))
pixels.show()

# Main loop will run forever
while True:
    flasher = MorseFlasher(random.choice(flash_color))  # Create a morse flasher object.
    flasher.encode(message)