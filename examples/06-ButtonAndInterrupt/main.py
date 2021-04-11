import machine, utime

bPressed = False

# Define the GPIO used for the LED and for the Button
led = machine.Pin(15,machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Attach an event handler to the button (RISING event)
button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_pressed)


def button_pressed(pin):
    global bPressed
    if not bPressed:
        bPressed = True     # set the bPressed var to True
        print(pin)          # display the pin associated to the button that trigger the function
        led.toggle()        # change the led status




