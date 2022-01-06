from uyeelight import *
from machine import Pin
import network
import time

# Available pins
class GPIO:
    D1 = 5
    D2 = 4
    D5 = 14
    D6 = 12
    D7 = 13

led = Pin(GPIO.D2, Pin.OUT)
btn1 = Pin(GPIO.D5, Pin.IN)
btn2 = Pin(GPIO.D6, Pin.IN)
btn3 = Pin(GPIO.D7, Pin.IN)

bulb = Bulb("192.168.1.51")

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

def main():
    last1 = 0
    last2 = 0
    last3 = 0

    while(True):

        val = btn1.value()
        if last1 == 0 and val == 1:
            print("toggle")
            try:
                bulb.toggle()
            except:
                print("Bulb error!")
            finally:
                time.sleep(0.3)
        last1 = val

        val = btn2.value()
        if last2 == 0 and val == 1:
            print("on")
            try:
                bulb.turn_on()
            except:
                print("Bulb error!")
            finally:
                time.sleep(0.3)
        last2 = val

        val = btn3.value()
        if last3 == 0 and val == 1:
            print("off")
            try:
                bulb.turn_off()
            except:
                print("Bulb error!")
            finally:
                time.sleep(0.3)
        last3 = val

while True:
    # wait until WiFi is connected, you need to configure it beforehand
    if sta_if.isconnected():
        main()
        break
