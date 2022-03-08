from machine import Pin, PWM
from time import sleep

class FancyLED():
    def __init__(self, pin):
        self.led = Pin(pin, Pin.OUT)
        frequency = 5000
        self.led_pwm = PWM(self.led, frequency)

    def fade(self, state, length):
        if length == 0:
            if state:
                self.led.on()
            else:
                self.led.off()
        else:
            length = length * 0.001
            if state:
                for duty_cycle in range(0, 1024):
                    self.led_pwm.duty(duty_cycle)
                    sleep(length)
            else:
                for duty_cycle in range(0, 1024):
                    self.led_pwm.duty(1024 - duty_cycle)
                    sleep(length)

    def flash(self, times):
        for i in range(times):
            self.fade(True, 0.5)
            self.fade(False, 1)
            sleep(0.3)