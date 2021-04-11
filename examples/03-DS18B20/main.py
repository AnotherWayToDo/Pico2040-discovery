import machine, onewire, ds18x20, time

ds_pin = machine.Pin(16)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
nDev = len(roms)

if (nDev == 0):
    print('No DS18x20 device found')
else:
    print('Nb device found : {}'.format(nDev))
    for d in roms:
        addr = ''.join(['{:02x}'.format(b) for b in d])
        print(addr)



    while True:
        ds_sensor.convert_temp()
        time.sleep_ms(750)
        for d in roms:
            addr = ''.join(['{:02x}'.format(b) for b in d])
            print('{} {}'.format(addr,  ds_sensor.read_temp(d)))
        time.sleep(5)