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

# Init Scenes
scene = Scene(bulbs)

# Init WiFi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)


# Interface handler
def main():
    while True:
        button = buttons.get_status()

        if button == 0:
            scene.set(scene.OFF)
            led.flash(1)
        elif button == 1:
            scene.set(scene.EVENING)
            led.flash(1)
        elif button == 2:
            scene.set(scene.BRIGHT)
            led.flash(1)
        elif button == 3:
            scene.set(scene.WARM)
            led.flash(1)
        elif button == 4:
            scene.set(scene.DIM)
            led.flash(1)
        elif button == 5:
            scene.set(scene.CREATIVE)
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
