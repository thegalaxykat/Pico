import machine
import utime

# assigns the onboard LED, pin 25, to the variable led_onboard
led_onboard = machine.Pin(25, machine.Pin.OUT)

while True:
    led_onboard.toggle()
    utime.sleep(1)
