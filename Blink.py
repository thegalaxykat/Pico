import machine
import utime

# assigns the onboard LED, pin 25, to the variable led_onboard
led_onboard = machine.Pin(25, machine.Pin.OUT)

while True:
     # turn on LED
     led_onboard.value(1) 
     utime.sleep(1)

     # turn off LED
     led_onboard.value(0)
     utime.sleep(1)
