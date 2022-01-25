from uyeelight import *
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

led = Pin(GPIO.D2, Pin.OUT)
btn1 = Pin(GPIO.D5, Pin.IN)
btn2 = Pin(GPIO.D6, Pin.IN)
btn3 = Pin(GPIO.D7, Pin.IN)

btbig = Pin(GPIO.D1, Pin.IN)

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

# Interface handler.
def main():

    last1 = 0
    last2 = 0
    last3 = 0

    while(True):

        val = btn1.value()
        if last1 == 1 and val == 0:
            Scene.set(bulbs, Scene.OFF)
        last1 = val

        val = btn2.value()
        if last2 == 1 and val == 0:
            Scene.set(bulbs, Scene.WARM)
        last2 = val

        val = btn3.value()
        if last3 == 1 and val == 0:
            Scene.set(bulbs, Scene.CREATIVE)
        last3 = val

while True:
    # Wait until WiFi is connected, you need to configure it beforehand.
    if sta_if.isconnected():
        main()
