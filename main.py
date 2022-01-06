from uyeelight import *
import network

bulb = Bulb("192.168.1.51")

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

while True:

    # wait until WiFi is connected, you need to configure it beforehand
    if sta_if.isconnected():

        try:
            bulb.turn_on()
        except YeeLightException as e:
            print(e)
        except:
            print("An error ¯\_(ツ)_/¯")

        break
