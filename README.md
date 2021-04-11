# Pico2040-discovery

## Board informations 

![](_img/Pico-R3-Pinout.png)


## Upload a project 
To upload a program on the Pi Pico and make it the default program that will run on the board at boot, then simply save your program in a **main.py** file directly on the board.

Using VS Code, it seem to have a little bug when you've a workspace with multiple project folder. To avoid any problem, open the folder you want to uplad directly in VS Code.

## Examples : 
- **blink** and **blinkExternalLed** show how to declare and use GPIO.

### Blinky External LED
This example show how to use GPIO in output mode.
![](examples/02-BlinkyExternalLed/01_External_LED.png)

## Notes on the examples shared 

### DS18B20 in parasite mode
In the parasite mode, I've had to change the resistor value to something lower than the requested 4.7KOhms. I don't know why.

![](examples/04-DS18B20_ParasiteMode/04_DS18B20_2x_parasite_mode.png)

Explanation for the parasite mode : https://learn.openenergymonitor.org/electricity-monitoring/temperature/DS18B20-temperature-sensing?redirected=true

