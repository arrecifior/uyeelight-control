from uyeelight import Bulb, Preset, Scene
from ufancyled import FancyLED
from machine import Pin
from time import sleep
import network

# Available pins
class GPIO:
    D1 = 5
    D2 = 4
    D5 = 14
    D6 = 12
    D7 = 13

bulbs = ['192.168.1.51',
         '192.168.1.54',
         '192.168.1.46',
         '192.168.1.55']

# Init I/O
led = FancyLED(GPIO.D2)
btn1 = Pin(GPIO.D5, Pin.IN, Pin.PULL_UP)
btn2 = Pin(GPIO.D6, Pin.IN, Pin.PULL_UP)
btn3 = Pin(GPIO.D7, Pin.IN, Pin.PULL_UP)

# Indicate startup
led.fade(True, 2)

# Init WiFi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

# Interface handler.
def main():

    last1 = 0
    last2 = 0
    last3 = 0

    while(True):

        val = btn1.value()
        if last1 == 0 and val == 1:
            Scene.set(bulbs, Scene.OFF)
            led.flash(1)
        last1 = val

        val = btn2.value()
        if last2 == 0 and val == 1:
            Scene.set(bulbs, Scene.WARM)
            led.flash(2)
        last2 = val

        val = btn3.value()
        if last3 == 0 and val == 1:
            Scene.set(bulbs, Scene.CREATIVE)
            led.flash(3)
        last3 = val

while True:
    # Wait until WiFi is connected, you need to configure it beforehand.
    if sta_if.isconnected():
        led.fade(False, 1.5) # Indicate startup complete
        main()
