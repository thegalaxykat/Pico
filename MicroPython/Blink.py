import machine
import utime

#assigns the onboard LED, pin 25, to the variable led_onboard
led_onboard = machine.Pin(25, machine.Pin.OUT)
led_red = machine.Pin(12, machine.Pin.OUT)
led_blue = machine.Pin(13, machine.Pin.OUT)
led_green = machine.Pin(14, machine.Pin.OUT)
led_yellow = machine.Pin(15, machine.Pin.OUT)

led_onboard.toggle()

while True:

    led_red.toggle()
    utime.sleep(.7)
    led_blue.toggle()
    utime.sleep(.7)
    led_green.toggle()
    utime.sleep(.7)
    led_yellow.toggle()
    utime.sleep(.7)
