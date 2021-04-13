import machine
import utime

machine.Pin(25, machine.Pin.OUT).value(1)

# sets the pin as INPUT and a PULL DOWN resistor (meaning that the non-pressed value is 0) 
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
led_red = machine.Pin(15, machine.Pin.OUT)
led_blue = machine.Pin(13, machine.Pin.OUT)

times_pressed = 0

while True:
    if button.value() == 1:
        times_pressed += 1
        if(times_pressed % 2) != 0:
            print("red led")
            led_blue.value(0)
            led_red.value(1)
            utime.sleep(.5)
        else:
            print("blue led")
            led_blue.value(1)
            led_red.value(0)
            utime.sleep(.5)
