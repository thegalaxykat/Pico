import machine
import utime

machine.Pin(25, machine.Pin.OUT).value(1)

# sets the pin as INPUT and a PULL DOWN resistor (meaning that the non-pressed value is 0) 
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        print("You see a button, you push the button. Simple as that.")
        utime.sleep(1)