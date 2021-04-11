#   This version is based on the 03-DS18B20 ... I've just add comment and a function
# to convert 1wire device addr in a string.

import machine, onewire, ds18x20, time

ds_pin = machine.Pin(16)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

# Function to transform an array of byte in hex string
# Used to get a human version of the 1wire addr 
def arrayByteToString(array):
    return ''.join(['{:02x}'.format(b) for b in array])


# Scan the 1wire bus
roms = ds_sensor.scan()
nDev = len(roms)


# In function of the number of devices found ...
if (nDev == 0):
    # ... no device found
    print('No DS18x20 device found')
else:
    # ... devices found : then get their addr ...
    print('Nb device found : {}'.format(nDev))
    for d in roms:
        addr = arrayByteToString(d)
        print(addr)

    # ... enter an infinite loop to get t° of each devices found
    while True:
        ds_sensor.convert_temp()
        time.sleep_ms(1000)
        for d in roms:
            print('{} {}'.format(arrayByteToString(d),  ds_sensor.read_temp(d)))
        time.sleep(5)
        