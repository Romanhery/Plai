"""
Plai MacroPad

Roman
"""
print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler

#Pin Definitons
COL0
COL1 = board.D0
COL2 = board.D1
COL3 = board.D2
ROW1 = board.D3
SDA = board.D4
SCL = board.D5
ROW2 = board.D6
ROW3 = board.D7
E11SWA = board.D8
E11SWB = board.D9

keyboard = KMKKeyboard()

keyboard.col_pins = (COL1,COL2,COL3)
keyboard.row_pins = (ROW1,ROW2,ROW3)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = (E11SWA,E11SWB,)