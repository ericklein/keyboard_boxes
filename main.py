#  Project Name:   keyboard_boxes
#  Developer:      Eric Klein Jr. (temp2@ericklein.com)
#  Description:    USB keyboard events from standard switches
# See README.md for target information, revision history, feature requests, etc.

import time
import board
from digitalio import DigitalInOut, Direction, Pull
# import digitalio #adafruit version
# from analogio import AnalogOut, AnalogIn  #why do we need it?

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_debouncer import Debouncer

print("imports ok")

# Your config!
# Set this to be which pins you're using, and what to do.
# For list of keycodes, see:
# https://circuitpython.readthedocs.io/projects/hid/en/latest/api.html
button_config = [
        # pin,     (Keycodes and modifier keycodes)
        [board.A1, (Keycode.SPACEBAR,) ],  # just a space
]
debouncers = []

#        [board.D2, (Keycode.A, Keycode.SHIFT, Keycode.GUI) ],# zoom mute
#        [board.D3, (Keycode.C, Keycode.CONTROL) ],
#        [board.D4, (Keycode.H, Keycode.GUI) ], # CMD-H hide

# start up the keyboardy-ness
#time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
kbd = Keyboard(usb_hid.devices)

print("keyboard init ok")

# Built in red LED
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT
button_light = DigitalInOut(board.D7)
button_light.direction = Direction.OUTPUT

print("LED setup ok")

# set up the pins and the debouncer on each pin
for (pin,*rest) in button_config:
        button = DigitalInOut(pin)
        button.direction = Direction.INPUT
        button.pull = Pull.UP
        debouncers.append( Debouncer(button) )

print("ready for main loop")

######################### MAIN LOOP ##############################
def main():
    while True:
        for i in range(len(button_config)):
            button = debouncers[i]
            button.update()

            (pin,keycodes) = button_config[i]
            print("button",i,"ready")
            if button.fell:
                print("push:",pin,"keycodes:",keycodes)
                #kbd.send(Keycode.SHIFT,Keycode.A)
                kbd.press(*keycodes)
                led.value = True
                button_light.value = True

            if button.rose:
                print("release:",pin)
                kbd.release(*keycodes)
                led.value = False
                button_light.value = False

            time.sleep(0.01)
######

# actually call main
main()