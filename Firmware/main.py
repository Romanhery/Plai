"""
Plai MacroPad

Roman
"""
print("Starting")

#Libraries
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display import Display , TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.media_keys import MediaKeys

#Pin Definitons
COL0 = board.D0
COL1 = board.D1
COL2 = board.D2
COL3 = board.D3
SDA = board.D4
SCL = board.D5
ROW0 = board.D6
ROW1 = board.D10
ROW2 = board.D7
EC11B = board.D9
EC11A = board.D8

keyboard = KMKKeyboard()

#Maping out the rows and the collums and what orientation the diodes are
keyboard.col_pins = (COL0,COL1,COL2,COL3)
keyboard.row_pins = (ROW0,ROW1,ROW2)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler = EncoderHandler()


#just adding the modules to the keyboard
keyboard.modules.append(encoder_handler)
keyboard.extensions.append(MediaKeys())

#Maping out the pins and the keys of the encoder
encoder_handler.pins = ((EC11A, EC11B, None, False),)
encoder_handler.map = (((KC.VOLD, KC.VOLU),),)

#mapping out all of the keys
keyboard.keymap = [
    [
        #Row 0
        KC.MPRV, #Previous Song
        KC.MPLY, #Play the Song
        KC.MNXT,  #Next Song
        KC.MUTE, #Mute Song

        #Row 1
        KC.LCTRL(KC.LALT(KC.LCMD(KC.LSHIFT(KC.V)))), # Vscode
        KC.LCTRL(KC.LALT(KC.LCMD(KC.LSHIFT(KC.F)))), # Fusion
        KC.LCTRL(KC.LALT(KC.LCMD(KC.LSHIFT(KC.D)))), # Davionci Resolve
        KC.NO,        # Empty matrix slot: We did this because the encoder doesnt have its own pin and we connected it to the matrix

        # ROW 2
        KC.LCTRL(KC.LALT(KC.LCMD(KC.LSHIFT(KC.K)))), # Ki Cad
        KC.LCTRL(KC.LALT(KC.LCMD(KC.LSHIFT(KC.C)))), # Chrome
        KC.LCTRL(KC.LALT(KC.LCMD(KC.LSHIFT(KC.F12)))),# Finder
        KC.NO,        # Empty matrix slot
    ]
]

#displays Coding Is Awesome!!!
display = Display(
    #Pin maping
    display=SSD1306(sda=SDA,scl=SCL),
    #What should go into the display
    entries=[
        #The actual text Coding is awesome
        TextEntry(text='Coding Is Awesome!!!')
    ],
    #how tall it should be
    height=32
)
#enter it into the actual display and show it
keyboard.extensions.append(display)

if __name__ == '__main__':
    keyboard.go()