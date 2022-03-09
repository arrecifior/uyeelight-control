from nis import match
from uyeelight import Scene
from ufancyled import FancyLED
from ubuttonhandler import ButtonHandler
from machine import Pin
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
led = FancyLED(GPIO.D1)
in1 = Pin(GPIO.D2, Pin.IN, Pin.PULL_UP)
in2 = Pin(GPIO.D5, Pin.IN, Pin.PULL_UP)
in3 = Pin(GPIO.D6, Pin.IN, Pin.PULL_UP)
in4 = Pin(GPIO.D7, Pin.IN, Pin.PULL_UP)

# Indicate startup
led.fade(True, 2)

# Init button handler
buttons = ButtonHandler(in1, in2, in3, in4)

# Init WiFi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

# Interface handler.
def main():
    while True:
        button = buttons.get_status()

        if button == 0:
            Scene.set(bulbs, Scene.OFF)
            led.flash(1)
        elif button == 1:
            Scene.set(bulbs, Scene.EVENING)
            led.flash(1)
        elif button == 2:
            Scene.set(bulbs, Scene.BRIGHT)
            led.flash(1)
        elif button == 3:
            Scene.set(bulbs, Scene.WARM)
            led.flash(1)
        elif button == 4:
            Scene.set(bulbs, Scene.DIM)
            led.flash(1)
        elif button == 5:
            Scene.set(bulbs, Scene.CREATIVE)
            led.flash(1)
        elif button == 6:
            pass
        elif button == 7:
            pass
        elif button == 8:
            pass

while True:
    # Wait until WiFi is connected, you need to configure it beforehand.
    if sta_if.isconnected():
        led.fade(False, 1.5) # Indicate startup complete
        main()
