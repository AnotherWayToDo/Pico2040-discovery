# A quick and dirty introduction to GPIO input

import machine, utime

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while(True):
    if (button.value() == 1):
        prnit("button pressed")
        utime.sleep(2)
